# Pyodbc Database Tools

This is a simple context manager for an odbc database connection using pyodbc.

# Prerequisites

You must have the following packages installed:

* libmyodbc
* unixodbc-bin
* unixodbc-dev

Copy and paste the below text for simplicity:

`sudo apt-get install libmyodbc unixodbc-bin unixodbc-dev`

If using mysql I have a script you can use to install mysql client and odbc packages for simple setup [here](https://gist.github.com/ziplokk1/18da3744f9fbed214503e99491e69c8f).

# Notes:

* This has only been tested using ubuntu 14.04LTS and windows 7