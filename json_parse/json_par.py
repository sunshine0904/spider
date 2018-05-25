#!/usr/bin/env python
# coding=utf-8

import json

'''
def parse json():
    f = open("1.json",encoding='utf-8')
    setting = json.load(f)
'''
with open("1.json",'r') as load_f:
    load_dict = json.load(load_f)
    #print(load_dict)
    
    global content

    for key,value in load_dict.items():
        if key == "date":
            print key+":"+value
        if key == "msgs":
            print type(key),key,type(value)
        
        content = value
       
        print type(content)
        for key in content:
            print type(key)
            if type(key)  != dict:
               continue
            for key,value in key.items():
                #print type(key),otype(value)
                print key
        


