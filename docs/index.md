# About

`Fbexport tool` is a thin wrapper for [fbexport](https://fbexport.sourceforge.net/), 
which is a program that exports and imports data from Firebird databases. The aim is to simplify the use of fbexport to extract a selection of tables in `csv` format. 

## Requirements

There is only one required program, 

* `fbexport`

which is called to backup a database. If you want to build the documentation then 
the following python packages are necessary.

* `mkdocs`
* `mkdocstrings`
* `mkdocs-material`

In adition, I use `pytest` for testing, but this is only a commodity as currently 
all testing is done by [doctest](https://docs.python.org/3/library/doctest.html). 


## Installation

## Ussage



Run fbexport-tool.py -h to see  details on how to use it.

The input to this program is an fdb database and a text file with a list of space 
separated names of tables to be exported or a list of the names of such tables.

This program is a thin wrap around fbexport, so you will need to install it before. In 
case your OS does not ship with the program, see