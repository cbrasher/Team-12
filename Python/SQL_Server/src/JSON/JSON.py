'''
Created on Oct 17, 2014

@author: Owner
'''

import json
import sqlite3
import threading, Queue
import serial

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

d = {'Sensor1':'17.12', 'Sensor2': '85.12', 'Sensor3':'45.63'}
j = json.dumps(d, sort_keys=True)
i = json.loads(j,object_hook=_decode_dict)
y= json.dumps(i)
print y
k = ("Sensor1","17.12","Sensor2","85.12","Sensor3","45.63")
l = json.dumps(k)
h = "Sensor 1"
m = "45.82"
n = "Sensor 2"
y = "65.83"
u = "Sensor 3"
p = "23.87"
g = (h,m,n,y,u,p)
print j
print i

db = sqlite3.connect("Test.sqlite")
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                      tester(id INTEGER PRIMARY KEY, Sensor_Name TEXT, Sensor_Value REAL, Sensor_Name1 TEXT, Sensor_Value1 REAL, Sensor_Name2 TEXT, Sensor_Value2 REAL)''')


cursor.execute('INSERT INTO tester (Sensor_Name, Sensor_Value,Sensor_Name1, Sensor_Value1,Sensor_Name2, Sensor_Value2) VALUES (?,?,?,?,?,?)',k)
db.commit()
query = 'INSERT INTO tester (Sensor_Name, Sensor_Value,Sensor_Name1, Sensor_Value1,Sensor_Name2, Sensor_Value2) VALUES (?,?,?,?,?,?)'
columns = ['Sensor_Name','Sensor_Value','Sensor_Name1','Sensor_Value1','Sensor_Name2','Sensor_Value2']
for data in i.iteritems():
    keys = (data[c] for c in columns)
    cursor.execute(query,keys)
db.commit()
db.close()