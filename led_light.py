#!usr/local/env/ python
from __future__ import print_function
import requests
import argparse
import urllib.request
import json
import numpy as np
from datetime import datetime as dt
import os
import RPi.GPIO as GPIO
import time

yellow=32
green=33
red=35
white=37

def light(dic_id,id_num,flag):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(yellow, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(white, GPIO.OUT)
    '''
    for i in dic_id:
        i['id'] == id_num:
            color = i['color']
    '''
    if id_num == 1:
        if flag == 1:
            GPIO.output(red, True)
        if flag == 0:
            GPIO.output(red, False)
    if id_num == 2:
        if flag == 1:
            GPIO.output(green, True)
        if flag == 0:
            GPIO.output(green, False)
    ''' 
    if color == 'red':
        if flag == 1:
	    GPIO.output(red, True)
        if flag == 0:
	    GPIO.output(red, False)
    if color == 'green':
        if flag == 1:
	    GPIO.output(green, True)
        if flag == 0:
	    GPIO.output(green, False)
    if color == 'yellow':
        if flag == 1:
	    GPIO.output(yellow, True)
        if flag == 0:
	    GPIO.output(yellow, False)
    if color == 'white':
        if flag == 1:
	    GPIO.output(white, True)
        if flag == 0:
	    GPIO.output(white, False)
    ''' 
    GPIO.cleanup()
