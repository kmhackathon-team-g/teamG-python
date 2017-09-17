#!usr/local/env/ python
from __future__ import print_function
import requests
import argparse
import urllib.request
import json
import numpy as np
from datetime import datetime as dt
import os

curl1 = "https://api.thingspeak.com/channels/332251/feeds.json?api_key=LIUIIAXK0HICC7OA&results=2"
r = urllib.request.urlopen(curl)
log = json.loads(r.read())
def light(dic_id,id_num,flag):
    for i in dic_id:
        i['id'] == id_num:
            color = i['color']
    if color == 'red':
        #if flag == 1 light red LED
        #if flag == 1 off red LED
    if color == 'green':
        #if flag == 1 light red LED
        #if flag == 1 off red LED
    if color == 'yellow':
        #if flag == 1 light red LED
        #if flag == 1 off red LED
    if color == 'white':
        #if flag == 1 light red LED
        #if flag == 1 off red LED
