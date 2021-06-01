import os
import pymysql

#GET username from Cloud9 workspace
#Modify this if running on different machine

username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #RUN A QUERY
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    #Close the connection regardless if above connection was a sucess
    connection.close()


