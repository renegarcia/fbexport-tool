# About

`Fbexport tool` is a thin wrapper for [fbexport](https://fbexport.sourceforge.net/),
which is a program that exports and imports data from Firebird databases. The aim is to
simplify the use of fbexport to extract a selection of tables in `csv` format. 

## Requirements

There is only one required program, 

* `fbexport`

which is called to backup a database. If you want to build the documentation then 
the following python packages are necessary.

* `mkdocs`
* `mkdocstrings`
* `mkdocs-material`

Dependencies are handled by [poetry](https://python-poetry.org/), in adition, I use 
`pytest` for testing, but this is only a commodity as currently all testing is done by 
[doctest](https://docs.python.org/3/library/doctest.html). 


## Installation

Running 

```sh
poetry install --no-root
```

should install a script `fbexport-tool` in your current virtual envirnoment. 


## Usage


First, make sure `fbexport` is installed somewhere in your path. 

The input to this program is a firebird database and a text file whose content is a list
of space separated names of the tables to be exported from the database. Alternatively,  
you can pass the table names as extra arguments to the command. Note that it is possible
to mix both the file and the list of names in the same calling to the program.

### Example

Given the following content in the current directory 

```
database.fbd
tables.txt
```

where the content of `tables.txt` is 

```
TABLE1
TABLE2
"SOME OTHER TABLE"
```

then calling 

```sh
fbexport-tool databse.fbd --tables tables.txt
```

will result in a new directory named `YYYY-MM-DD-HH-MM-SS-database` where
`YYYY-MM-DD-HH-MM-SS` is the system timestamp when the program was invoked and  whose
content consists of three csv files 

```
YYYY-MM-DD-HH-MM-SS-database
|
|-- table1.csv
|-- table2.csv
|-- some_other_table.csv
```

with the data of each table backed up.