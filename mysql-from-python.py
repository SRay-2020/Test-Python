import os
import datetime
import pymysql

# GET username from Cloud9 workspace
# Modify this if running on different machine

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # RUN A QUERY
    with connection.cursor() as cursor:
        row = ("Bob", 31, "1990-01-06 23:01:11")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit
      
finally:
    # Close the connection regardless if above connection was a sucess
    connection.close()
    