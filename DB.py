#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("192.168.100.198","root","5105458","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()