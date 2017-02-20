#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import numpy as np
import scipy as sp
import scipy.io as sio
import sys
import os
#import MySQLdb

dict_clean = {}

with open('train.txt','r') as f:
	for line in f.readlines():
		key_val = line[:-1].split(' ')
		dict_clean[key_val[0]] = key_val[1]


def CNNclean(para):
	global dict_clean
	return dict_clean[para]
       
def listpuredir(dir):
	fo = open('cb.txt','w+')
	list=os.listdir(dir)
	for line in list:
		path = dir+'/'+line
		print path
		rt=CNNclean(path)
		temp = path+'  '+str(rt)
		fo.write(temp)
		fo.write('\n')
		#print "%d" %(rt)
	fo.close()


checkdir="/home/wang/gf/image"
#listpuredir(checkdir)


#rt=gf("/home/second/tsinghua_image/test/FXPXC0120140410170244ZT003.jpg")
#print "%d" %(rt)
