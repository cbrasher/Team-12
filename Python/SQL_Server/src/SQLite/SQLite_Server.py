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
'''
Define some constants for the module to act on such as
file names, table names, columns and the types of columns
'''
'''
table_name1= 'Fence_Readings_1' #Note SQLite does not accept spaces in names
table_name2= 'Fence Readings 2'
row_id='Row_ID'
date_col = 'date' # name of the date column
time_col = 'time'# name of the time column
date_time_col = 'date_time' #name of date & time column
field_type0='INTEGER'
field_type1='REAL'
field_type2='TEXT'
field_type3='BLOB'
field_type4='NULL'

conn = sqlite3.connect(sqlite_file) #define the connection to the database
#Conn will connect to Fence.db or if there is no Fence.db will create an
#instance of it. 

cur = conn.cursor() #Cur will be our cursor for use in the database
#Cursors allow us to traverse the result set of the database(DB)


'''
'''
The Following execute will create the Table within our db file it can be given
the table name, column names along with column type, and can be given a primary 
key. This key is important as we gain a boost in perfomance on the query the database
using the primary key. Only one key can be assinged to a table but it can be multiple columns.
'''
'''
cur.execute('DROP TABLE Fence_Readings_1')

cur.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
                .format(tn=table_name1, nf=row_id, ft=field_type0))

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} "\
                .format(tn=table_name1, cn='Values_0', ct=field_type2))

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                .format(tn=table_name1, cn='Values_1', ct=field_type2))

cur.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (1, 'test')".\
                format(tn=table_name1, idf=row_id, cn='Values_1'))

cur.execute("UPDATE {tn} SET {cn}=('Hello World') WHERE {idf}=(1)".\
                format(tn=table_name1, cn='Values_0', idf=row_id))


cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name1, cn=date_time_col))
# update row for the new current date and time column, e.g., 2014-03-06 16:26:37
cur.execute("UPDATE {tn} SET {cn}=(CURRENT_TIMESTAMP) WHERE {idf}='1'"\
         .format(tn=table_name1, idf=row_id, cn=date_time_col))


cur.execute('SELECT * FROM {tn}'.\
        format(tn=table_name1))
all_rows = cur.fetchall()
print('1):', all_rows)


conn.commit() #Any chanes to the database other then sending queries must
#be commited by the commit() command
conn.close() #Connection to the database must be when we are done with our operations
'''
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