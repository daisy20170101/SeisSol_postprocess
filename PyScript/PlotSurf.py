#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import pyproj

xdmfFilename = 'result4/tp20m-surface.xdmf'
trench = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/trench.txt')

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm',zone='11N',ellps='WGS84', datum='WGS84')

ndt = ReadNdt(xdmfFilename)
xyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)

centers = (xyz[connect[:,0]] + xyz[connect[:,1]] + xyz[connect[:,2]])/3000.

surfxyz = pyproj.transform(lla, myproj, trench[:,0],trench[:,1],trench[:,2], radians=False)

uu = LoadData(xdmfFilename,'U',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
vv = LoadData(xdmfFilename,'V',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
ww = LoadData(xdmfFilename,'W',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)

slp1 = uu[0][:]
slp2 = vv[0][:]
slp3 = ww[0][:]

slp = np.sqrt(slp1**2 + slp2**2 + slp3**2)

#%%
plt.figure()

sc = plt.scatter(centers[::1,0],centers[::1,1],s=0.3, c=slp[::1],cmap='seismic',vmin=-0.002,vmax=0.002)
cl = plt.colorbar(sc)
cl.set_label('PGD (m)')

#plt.plot(x[:],y[:],'.k',markersize=0.1
plt.plot(c20[:,0],c20[:,1],'.k',markersize=0.1)
plt.plot(c40[:,0],c40[:,1],'.k',markersize=0.1)
plt.plot(c60[:,0],c60[:,1],'.k',markersize=0.1)
plt.plot(c80[:,0],c80[:,1],'.k',markersize=0.1)
plt.plot(c5[:,0],c5[:,1],'-k',markersize=0.1)

plt.xlim( [-500, 700])
plt.ylim( [-500, 300])

plt.show()






    
