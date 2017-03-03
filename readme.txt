Please refer to the article:
https://www.tutorialspoint.com/python/python_database_access.htm

Python MySQL Database Access

The Python standard for database interfaces is the Python DB-API. Most Python database interfaces adhere to this standard.

You can choose the right database for your application. Python Database API supports a wide range of database servers such as −

    GadFly

    mSQL

    MySQL

    PostgreSQL

    Microsoft SQL Server 2000

    Informix

    Interbase

    Oracle

    Sybase

Here is the list of available Python database interfaces: Python Database Interfaces and APIs .You must download a separate DB API module for each database you need to access. For example, if you need to access an Oracle database as well as a MySQL database, you must download both the Oracle and the MySQL database modules.

The DB API provides a minimal standard for working with databases using Python structures and syntax wherever possible. This API includes the following:

    Importing the API module.

    Acquiring a connection with the database.

    Issuing SQL statements and stored procedures.

    Closing the connection

We would learn all the concepts using MySQL, so let us talk about MySQLdb module.