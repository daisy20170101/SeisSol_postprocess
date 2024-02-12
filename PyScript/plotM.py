#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:28:14 2018

@author: dli
"""

import numpy as np
import matplotlib.pyplot as plt

folder = 'result4/'
#modelname = 'data6'
modelname = 'tp20h'

fin = open(folder+modelname+'-EnF_0t-all.dat','r')
enf = np.loadtxt(fin,comments='#',skiprows=1)

mfile='STF_usgs.txt'
fin2 = open(mfile,'r');
mr = np.loadtxt(fin2);
    
plt.figure()

#plt.subplot(1,2,1)               
plt.plot(enf[:,0],enf[:,1]*1e7/1e26,'-r')   # from MPa*m**2/s to dyne-cm/s
plt.plot(mr[:,0],mr[:,1]/1e19,'-k')
plt.legend(['this study','USGS'])

plt.xlabel('time (s)')
plt.ylabel('moment rate/1e19 (Nm/s)')     
plt.xlim([0,100])
plt.ylim([0,9])


# seismic moment magnitude
moment0 = 0.0
M0 = np.trapz(enf[:,1], x=enf[:,0])

mag  = 2/3*np.log10(M0)-6.07

plt.title('Mw:'+str(round(mag,2)))
plt.savefig(modelname+'-mag.png',dpi=150)                


