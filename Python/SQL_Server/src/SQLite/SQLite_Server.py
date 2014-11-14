'''
Created on Oct 12, 2014

@author: BBC
'''



'''
This code is the sqlite module of the server
It will allow access to a SQLite database
In that database values will be stored for use in 
other modules within the server
'''

'''
First we need to import the sqlite3 module into the
program which will give us access to the database
'''
import sqlite3
import random


sqlite_file =  'C:/ECEN 403/SQLite Database/Fence.db'
try:
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(sqlite_file)
    # Get a cursor object
    cursor = db.cursor()
    # Check if table users does not exist and create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Fence_Readings(id INTEGER PRIMARY KEY, value0 INTEGER, value1 REAL, value2 INTEGER, Sensor_Name TEXT)''')
    # Commit the change
    db.commit()
    rowid = 0
    while True:
        newvalue0=random.randint(1,10)
        newvalue1=random.randrange(1,100)
        newvalue2=random.random()
        sensorname=random.choice('abcdefg')
        cursor.execute('INSERT INTO Fence_Readings (value0, value1, value2, Sensor_Name) VALUES (?,?,?,?)',(newvalue0,newvalue1,newvalue2,sensorname))
        rowid = rowid + 1
        db.commit()
        if rowid == 5:
            break
    while rowid==5:
        cursor.execute('SELECT id, value0, value1, value2, Sensor_Name FROM Fence_Readings')
        for row in cursor:
            print('{0} : {1}, {2}, {3}, {4}'.format(row[0],row[1],row[2],row[3],row[4]))
            rowid=rowid+1
# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()