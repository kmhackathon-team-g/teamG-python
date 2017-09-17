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
curl2 = "https://api.thingspeak.com/channels/332335/feeds.json?api_key=O81NGSHFYAASSUFP&results=2"

def data_load(curl,id_num):
    r = urllib.request.urlopen(curl)
    log = json.loads(r.read().decode("utf-8"))
    timestmp = log['channel']['updated_at']
    if os.path.exists('./tmstmplog{}.txt'.format(id_num)) == False:
        with open('tmstmplog{}.txt'.format(id_num),'w') as f:
            f.write(timestmp)
    with open('tmstmplog{}.txt'.format(id_num),'r') as f:
        tm_log = f.read()
    d = dt.strptime(timestmp,'%Y-%m-%dT%H:%M:%SZ')
    d_log = dt.strptime(tm_log,'%Y-%m-%dT%H:%M:%SZ')
    d_delta = d - d_log
    t_delta = str(d_delta)
    #print(d_delta)
    with open('tmstmplog{}.txt'.format(id_num),'w') as f:
        f.write(timestmp)
    if t_delta[0:1] ==  '0' and t_delta[2:4] == '00' and t_delta[5:7] == '00':
        print(0)
        return 0
    else:
        print(1)
        return 1
    '''
    tm_array = np.asarray([int(timestmp[11:13]),int(timestmp[14:16]),int(timestmp[17:19])])
    tm_log = np.load('tmstmplog.npy')
    print(tm_log)
    np.save('tmstmplog.npy',tm_array)
    '''
#data_load(curl1,1)
#data_load(curl2,2)
