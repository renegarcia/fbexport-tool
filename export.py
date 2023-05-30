def export_cmd(
    database: str, destination: str, table: str, password: str = "masterkey"
) -> str:
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

    >>> export_cmd('database.gbd', destination='database.csv', table='MYTABLE')
    'fbexport -S -D database.gbd -P masterkey -F database.csv -V MYTABLE'
    """
    return f"fbexport -S -D {database} -P {password} -F {destination} -V {table}"
