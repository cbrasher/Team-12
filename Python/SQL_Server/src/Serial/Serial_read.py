'''
Created on Oct 12, 2014

@author: Owner
'''
from time import sleep
import sqlite3
import serial
import json

ser = serial.Serial('COM7', 57600)



db = sqlite3.connect("C:/ECEN 403/SQLite Database/Fence.db")
cursor = db.cursor()
'''
Create a User Input that could decide to drop recent table, 
create a new table, skip portions of the bode, or exit program immediately
'''
cursor.execute('''Drop TABLE Field_Readings''')
db.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Field_Readings(id INTEGER PRIMARY KEY, Sensor_Name TEXT, Sensor_Value REAL, Sensor_Name1 TEXT, Sensor_Value1 REAL, Sensor_Name2 TEXT, Sensor_Value2 REAL)''')
db.commit()

data = '{'+ser.readline()+'}'

try:
    while data != None:
        data = '{'+ser.readline()+'}'
        print data  #debugging component 
        #Do not print anything else on the serial line on the teensy or the python server will
        #flip its collective shit!!!!!
        decode_d2 = json.loads(data)
        print decode_d2
        b0 = decode_d2["id1"] #name
        b1 = decode_d2[b0] #value
        b2 = decode_d2["id2"]
        b3 = decode_d2[b2]
        b4 = decode_d2["id3"]
        b5 = decode_d2[b4]
        readings = [b0, b1, b2, b3, b4, b5]
        
    
        cursor.execute('INSERT INTO Field_Readings (Sensor_Name, Sensor_Value,Sensor_Name1, Sensor_Value1,Sensor_Name2, Sensor_Value2) VALUES (?,?,?,?,?,?)',readings)
        db.commit()
        
        
        
        
    #Then Write Processed data back
    #ser.write(char(data goes here)) #writes back over serial line to teensy 
finally:
    print 'Done'
    db.close()