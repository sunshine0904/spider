#!/usr/bin/env python
# coding=utf-8

#import simplejson as json
import json

with open("../2018-2-10-daily.json",'r') as load_f:
    parse_json = json.load(load_f)
    #print parse_json
    all_msgs=parse_json['msgs']
    print parse_json['date']
    
    for key in all_msgs:
        #print type(key),key
        #print key['id'],":",key['loginname'],
        print "[",key['realname'],"]",":",key['msg'],"\r\n"

