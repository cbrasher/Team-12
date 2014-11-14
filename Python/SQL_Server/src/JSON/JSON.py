

import json
#import sys
import sqlite3
import random
from time import sleep
from cmath import acos, sqrt
from math import fsum

db = sqlite3.connect("C:/ECEN 403/SQLite Database/Fence.db")
cursor = db.cursor()
#cursor.execute('''Drop TABLE tester''')
db.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                      tester(id INTEGER PRIMARY KEY, Sensor_Name TEXT, Sensor_Value REAL, Sensor_Name1 TEXT, Sensor_Value1 REAL, Sensor_Name2 TEXT, Sensor_Value2 REAL)''')
db.commit()
bunny = 1
moonbear = 1
i = 0
moon = []
luna = []
while bunny <= 5:
    p0 = '"id' + str(bunny)+'"'
    bunny += 1
    luna.append(p0)
while moonbear <= 4:
    p1 = '"Sensor' + str(moonbear)+'"'
    moonbear += 1
    moon.append(p1)
    
try:
    while i<=1000:
        a = random.randrange(0.00,500.00)
        b = random.randrange(0.00,500.00)
        c = random.randrange(0.00,500.00)
    
        data = '{' + luna[0] + ' : ' + moon[0] + ','+ moon[0] + ' : '+ str(a) +','+ luna[1] + ' : ' + moon[1] + ',' + moon[1] + ' : '+ str(b)+ ',' + luna[2] + ' : ' + moon[3] + ','  + moon[3] + ' : ' + str(c)+'}'
        print data
        sleep(.5)
        
        ###################
        decode_d2 = json.loads(data)
        b0 = decode_d2['id1']
        b1 = decode_d2[b0]
        b2 = decode_d2["id2"]
        b3 = decode_d2[b2]
        b4 = decode_d2["id3"]
        b5 = decode_d2[b4]
        list1 = [b0, b1, b2, b3, b4, b5]
        ###################
        
        ###################
        list2 = [b1,b3,b5]
        avg=sum(list2)/len(list2)
        a = min(list2)
        b = max(list2)
        print a
        print b
        c = a - b
        d = b - a
        print c
        print d
        e = random.randrange(1,10)
        print range(len(list2))
        print fsum(list2)
        print sqrt(avg)
        print acos(avg)
        print avg
        ###################
        
        sleep(5)
        
        cursor.execute('INSERT INTO tester (Sensor_Name, Sensor_Value,Sensor_Name1, Sensor_Value1,Sensor_Name2, Sensor_Value2) VALUES (?,?,?,?,?,?)',list1)
        db.commit()
        i += 1
finally:
    print 'Done'
    db.close()