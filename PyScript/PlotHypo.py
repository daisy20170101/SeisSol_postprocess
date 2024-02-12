#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import pyproj
#import scipy.io as sio
import matplotlib.tri as tri
from mpl_toolkits.basemap import Basemap

modelname = 'alkR057-TP49'
foldername = '/import/deadlock-data/dli/Alaska2021/resultNew/'

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='geocent', init='EPSG:5936',ellps='WGS84', datum='WGS84')

xdmfFilename =foldername + modelname+'-fault.xdmf'

stall = np.loadtxt('hypocenters.dat')
staxyz= pyproj.transform(lla, myproj, stall[:,0],stall[:,1], stall[:,1], radians=False)


surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)-1

td0= LoadData(xdmfFilename,'Td0',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)

triang = tri.Triangulation(surfxyz[:,0]/1e3,surfxyz[:,1]/1e3,connect)

FidReceiversnew = 'hypo_xyz.txt'

dd = np.loadtxt(FidReceiversnew)
fig,ax0=plt.subplots(nrows=1,ncols=1,figsize=(5,3.5))

ax0.plot(dd[3:,0]/1e3,dd[3:,1]/1e3,'*k',markersize=3)
ax0.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))
ax0.plot(dd[0,0]/1e3,dd[0,1]/1e3,'*r',markersize=3)

sc = ax0.tripcolor(triang,td0[0]/1e6,cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax0)

plt.title('hypocenter')
plt.savefig('hypocenters.png',dpi=200)
    
