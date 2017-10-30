#!/usr/bin/python3
#
# Extract IOC's from MISP
#
# Author: Xavier Mertens <xavier@rootshell.be>
#
# Copyright: GPLv3 (http://gplv3.fsf.org/)
# Feel free to use the code, but please share the changes you've made
#
import sys
import os
import json
import urllib3
from optparse import OptionParser
from pymisp import PyMISP

# Read default value from the local config file
try:
        from mispconfig import server, authkey, sslcheck
except:
        pass

try:
        dict = eval(sys.argv[1])
except:
        pass

if server not in dict:
        if server == None:
                print("No server defined")
else:
        server = dict['server']
if authkey not in dict:
        if authkey == None:
                print("No authkey defined")
else:
        authkey = dict['authkey']
if sslcheck not in dict:
        if sslcheck == None:
                print("No sslcheck defined")
else:
        sslcheck = dict['sslcheck']

def init(url, key, ssl):
    return PyMISP(url, key, ssl, 'json')

def get_event(m, e):
        result = m.get_event(e)
        return result['Event']['Attribute']

def get_last(m, l):
        result = m.download_last(l)
        data = []
        for r in result['response']:
                for a in r['Event']['Attribute']:
                        data.append(a)
        return data

try:
        misp = init(server, authkey, False)
except:
        exit(1)

if 'eventid' in dict:
        print(str(get_event(misp, dict['eventid'])))
elif 'last' in dict:
        print(str(get_last(misp, dict['last'])))
else:
        exit(1)

exit(0)