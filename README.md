# fbexport-tool.py

A tool to export data from a firebird database in bulk. Run `fbexport-tool.py -h` to
see details on how to use it.

The input to this programm is an fdb database and a text file with a list of space
separated names of tables to be exported or a list of the names of such tables.

This programm is a thin wrap around `fbexport`, so you will need to install it before.
In case your OS does not ship with the program, see

[http://www.firebirdfaq.org/fbexport.php](http://www.firebirdfaq.org/fbexport.php)