import json 
import pathlib
from sys import path

FILE_NAME = 'user.json'


#creates if not exists + 
# append new json 
def add_new_user(username,password):
    try:
        f = open(FILE_NAME,'r')
        data_dict = json.loads(f.read())
        f.close()
        f = open(FILE_NAME,'w')
    except FileNotFoundError as e :
        f = open(FILE_NAME,'x+')
        data_dict = {}
        
    if username in data_dict:
        f.write(json.dumps(data_dict))
        raise ValueError('User Exists !')
    
    data_dict[username] = {
        'password' : password,
        'cart' : []
    }
    f.write(json.dumps(data_dict))
    f.close()

def read_json_file() :
    try:
        f = open(FILE_NAME,'r')
        return json.loads(f.read())
    except FileNotFoundError as e :
        return {}

add_new_user('navid','123456')
add_new_user('Nane_ghmr','101010')
add_new_user('Nane_soghra','101010')

print(read_json_file())