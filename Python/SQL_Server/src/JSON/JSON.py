
''' Ignore this for now
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

d = { "Sensor1": 17.12, "Sensor2": 85.12, "Sensor3": 45.63}
a = []
b = 0
if b < 10:
    a.append(d)
print a
for b in range(0,1):
    b += 1
    a.pop()
print a
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
print a

'''
import json
import sqlite3
import random
from time import sleep

db = sqlite3.connect("Test.sqlite")
cursor = db.cursor()
#cursor.execute('''Drop TABLE tester''')
db.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                      tester(id INTEGER PRIMARY KEY, Sensor_Name TEXT, Sensor_Value REAL, Sensor_Name1 TEXT, Sensor_Value1 REAL, Sensor_Name2 TEXT, Sensor_Value2 REAL)''')
db.commit()
i = 0
str1 = '"Sensor1"'
try:
    while i<=1000:
        a = random.randrange(0.00,500.00)
        b = random.randrange(0.00,500.00)
        c = random.randrange(0.00,500.00)
    
        data = '{' '"id1"' + ' : ' + str1 + ','+ '"Sensor1"' + ' : '+ str(a) +','+ '"id2"' + ' : ' + '"Sensor2"' + ',' + '"Sensor2"' + ' : '+ str(b)+ ',' + '"id3"' + ' : ' + '"Sensor3"' + ','  + '"Sensor3"' + ' : ' + str(c)+'}'

        decode_d2 = json.loads(data)
        b0 = decode_d2["id1"]
        b1 = decode_d2[b0]
        b2 = decode_d2["id2"]
        b3 = decode_d2[b2]
        b4 = decode_d2["id3"]
        b5 = decode_d2[b4]
        list1 = [b0, b1, b2, b3, b4, b5]
    
        '''d0 = '{"id1" : "Sensor1" ,"Sensor1" : 17.12, "id2" : "Sensor2", "Sensor2" : 85.12, "id3" : "Sensor3", "Sensor3": 45.63}'
        decode_d0 = json.loads(d0) #need to give json parameter in decode to seperate terms into respective fields 
        a0 = decode_d0["id1"]
        a1 = decode_d0[a0]
        a2 = decode_d0["id2"]
        a3 = decode_d0[a2]
        a4 = decode_d0["id3"]
        a5 = decode_d0[a4]
        list0 = [a0, a1, a2, a3, a4 ,a5]
        print list0'''
    
        cursor.execute('INSERT INTO tester (Sensor_Name, Sensor_Value,Sensor_Name1, Sensor_Value1,Sensor_Name2, Sensor_Value2) VALUES (?,?,?,?,?,?)',list1)
        db.commit()
        print "Computing"
        i += 1
finally:
    print 'Done'
    db.close()