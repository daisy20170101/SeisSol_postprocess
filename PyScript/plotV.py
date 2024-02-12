#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:28:14 2018

@author: dli
"""

import numpy as np
import matplotlib.pyplot as plt

folder = 'output/'
model = 'data5'
fin1 = open(folder+model+'-receiver-00001-00011.dat','r')
fin2 = open(folder+model+'-receiver-00002-00008.dat','r')
fin3 = open(folder+model+'-receiver-00003-00016.dat','r')

dd1 = np.loadtxt(fin1,comments='#',skiprows=2)
dd2 = np.loadtxt(fin2,comments='#',skiprows=2)
dd3 = np.loadtxt(fin3,comments='#',skiprows=2)

plt.figure(figsize=(9,4))
               
plt.subplot(1,2,1)               
plt.plot(dd1[:,0],dd1[:,7])  
plt.plot(dd2[:,0],dd2[:,7])  
plt.plot(dd3[:,0],dd3[:,7])  
#plt.plot(dd3[:,0],dd3[:,2]) 

#plt.plot(dd[:,0],dd[:,9])  
plt.legend(['u'])
plt.xlabel('time')
plt.ylabel('velocity (m/s)')     

plt.subplot(1,2,2)
#plt.plot(dd1[:,0],dd1[:,7])   
plt.plot(dd1[:,0],dd1[:,8])  
plt.plot(dd2[:,0],dd2[:,8])  
plt.plot(dd3[:,0],dd3[:,8]) 
#plt.plot(dd3[:,0],dd3[:,7])  
plt.legend(['v'])

outname = model+'-vel.png'
plt.savefig(outname,dpi=150,transparent=False)
