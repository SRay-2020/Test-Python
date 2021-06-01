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
        rows = [("Bill", 51, "1970-03-09 21:01:07"),
                ("Jim", 100, "1920-09-09 10:19:34"),
                ("Fred", 10, "2010-12-12 06:01:11")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
      
finally:
    # Close the connection regardless if above connection was a sucess
    connection.close()
    