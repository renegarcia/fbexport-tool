from pathlib import Path
from datetime import datetime
from os import makedirs
from typing import Iterator
import string
import io
import subprocess


def export_cmd(
    database: str, destination: str, table: str, password: str = "masterkey"
) -> list[str]:
    """
    return a `fbexport` statement suitable for use in the terminal.

    Parameters

    @param database: Database location or path.
    @password
    @destination: Output location or path.
    @table: The name of the table to export.

    Returns

    A string representing the command that should be executed to commit the export.

    Example

    >>> export_cmd('database.fbd', destination='database.csv', table='MYTABLE')
    ['fbexport', '-H', '', '-Sc', '-J', 'Y-M-D', '-D', 'database.fbd', '-F', 'database.csv', '-V', 'MYTABLE']
    """
    return [
        "fbexport",
        "-H",
        "",
        "-Sc",
        "-J",
        "Y-M-D",
        "-D",
        database,
        "-F",
        destination,
        "-V",
        table,
    ]


def extract(database: str, table: str, outputdir: str, verbose: bool = True):
    dest = Path(outputdir).joinpath(table_csv_filename(table))
    cmd = export_cmd(database, dest, table)
    if verbose:
        print(f"Extracting {table} into {outputdir}")
    subprocess.run(cmd)
    if verbose:
        print("Done")


def outputdir_filename(database: Path | str, when: datetime) -> str:
    """
    Returns the name of the output directory in format YYYY-MM-DD-hh-mm-ss-database
    with the database suffix removed.
    If the database name has spaces they are replaced by underscores (i.e. `"database name".fdb` is replaced by `database_name`)

    Example

    >>> from datetime import datetime
    >>> when = datetime(2023, 1, 1, 14,0,0)
    >>> outputdir_filename('database.fdb', when)
    '2023-01-01-14-00-00-database'

    >>> outputdir_filename('another database.fdb', when)
    '2023-01-01-14-00-00-another_database'
    """
    if isinstance(database, str):
        database = Path(database)
    dtime = when.strftime("%Y-%m-%d-%H-%M-%S")
    fname = database.stem.replace(" ", "_")
    return f"{dtime}-{fname}"


def table_csv_filename(tablename: str) -> str:
    """
    Returns a sanitized version of the name of a table. The name is converted to
    lowercase, any space is replaced by underscores and special caracters like
    quotes are stripped away.

    Examples

    >>> table_csv_filename('TABLE')
    'table.csv'

    >>> table_csv_filename('A TABLE')
    'a_table.csv'

    >>> table_csv_filename('"Decimal"')
    'decimal.csv'
    """
    translation_table = str.maketrans("", "", string.punctuation)
    cleaned = tablename.translate(translation_table)
    return cleaned.replace(" ", "_").lower() + ".csv"
    return tablename


def iter_words(stream: io.TextIOWrapper) -> Iterator[str]:
    """
    Return an iterator to the words contained in `stream`.

    Example

    >>> from io import StringIO
    >>> buffer = StringIO(initial_value=' word1 word2 \\n word3 ')
    >>> [w for w in iter_words(buffer)]
    ['word1', 'word2', 'word3']
    """
    for line in stream:
        for word in line.split():
            yield word


def main():
    parser = ArgumentParser(description="Export tables from a database file.")
    parser.add_argument("database")
    parser.add_argument("--tables_file", help="Table list filename")
    parser.add_argument("table", help="Zero or more tables to export", nargs="*")
    args = parser.parse_args()

    database = args.database
    tables = args.table
    tables_file = args.tables_file

    now = datetime.now()
    outputdir = outputdir_filename(database, when=now)
    makedirs(outputdir)

    for table in tables:
        extract(database, table, outputdir=outputdir)

    if tables_file:
        with open(tables_file) as f:
            for table in iter_words(f):
                extract(database, table, outputdir=outputdir)


if __name__ == "__main__":
    from argparse import ArgumentParser

    main()
