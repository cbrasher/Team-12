'''
Created on Nov 5, 2014

@author: Owner
'''
import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = demjson.encode(data)
print json

text = demjson.decode(json)
print text

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here

    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]