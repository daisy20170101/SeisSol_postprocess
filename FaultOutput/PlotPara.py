#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: D. Li
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import pyproj

#%%
modelname = 'f8'

xdmfFilename ='/import/freenas-m-05-seissol/dli/Mexico/lockingmodel2/'+modelname+'-fault.xdmf'

trench = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/trench.txt')
c5 = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/contour5.txt')
c20 = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/contour20.txt')
c40 = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/contour40.txt')
c60 = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/contour60.txt')
c80 = np.loadtxt('/import/deadlock-data/dli/Mexico/Launch_SeisSol/contour80.txt')

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm',zone='11N',ellps='WGS84', datum='WGS84')

ndt = ReadNdt(xdmfFilename)
xyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)

surfxyz = pyproj.transform(lla, myproj, trench[:,0],trench[:,1],trench[:,2], radians=False)

c20xyz = pyproj.transform(lla, myproj, c20[:,0],c20[:,1],c20[:,2], radians=False)
c40xyz = pyproj.transform(lla, myproj, c40[:,0],c40[:,1],c40[:,2], radians=False)
c60xyz = pyproj.transform(lla, myproj, c60[:,0],c60[:,1],c60[:,2], radians=False)
refer =  pyproj.transform(lla, myproj, -101,18,0, radians=False)

xtrch = surfxyz[0]/1000 - refer[0]/1000
ytrch = surfxyz[1]/1000 - refer[1]/1000

triang = tri.Triangulation(xyz[:,0]/1000,xyz[:,1]/1000,connect)

#%%
td1 = LoadData(xdmfFilename,'Td0',connect.shape[0],idt=1,oneDtMem=True,firstElement=-1)
pn1 = LoadData(xdmfFilename,'Pn0',connect.shape[0],idt=1,oneDtMem=True,firstElement=-1)
td0 = LoadData(xdmfFilename,'Td0',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)
pn0 = LoadData(xdmfFilename,'Pn0',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)

mud0 =  LoadData(xdmfFilename,'Mud',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)

R   = - td0[0]/pn0[0]
cfs = np.abs(td1[0] + mud0[0]*pn1[0])
#s   = cfs/(-mud[0]*pn0[0]+0.1*pn0[0])

#%%

fig,([ax0,ax1],[ax2,ax3])=plt.subplots(nrows=2,ncols=2,figsize=(8,6))

sc = ax0.tripcolor(triang,td0[0]/1e6,cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax0)
cl.set_label('Td0 (MPa)')

ax0.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax0.plot(c20[:,0],c20[:,1],'.k',markersize=0.1)
#ax0.plot(c40[:,0],c40[:,1],'.k',markersize=0.1)
#ax0.plot(c60[:,0],c60[:,1],'.k',markersize=0.1)
#ax0.plot(c80[:,0],c80[:,1],'.k',markersize=0.1)
#plt.plot(c5[:,0],c5[:,1],'-k',markersize=0.1)

ax0.set(xlim=( -150, 150),ylim=(-200,100))
#ax0.set_title('Mapview of Td0')

sc = ax1.tripcolor(triang,-pn0[0]/1e6,cmap='plasma',shading='flat',vmin=0,vmax=50)
cl = fig.colorbar(sc,ax=ax1)
cl.set_label('Pn0 (MPa)')

ax1.set(xlim=(-150, 150),ylim=(-200,100))
ax1.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)

#ax1.set_title('Mapview of Pn0')

sc = ax2.tripcolor(triang,R,cmap='viridis',shading='flat',vmin=0.2,vmax=0.8)
cl = fig.colorbar(sc,ax=ax2)
cl.set_label('Td0/Pn0')

ax2.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
ax2.set(xlim=( -150, 150),ylim=(-200,100))

#ax2.set_title('Mapview of R0')

sc = ax3.tripcolor(triang,cfs/1e6,cmap='seismic',shading='flat')
cl = fig.colorbar(sc,ax=ax3)
cl.set_label('CFS (MPa)')

ax3.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
ax3.set(xlim=( -150, 150),ylim=(-200,100))

#ax2.set_title('Mapview of S')

outname = modelname+'-para.png'
plt.savefig(outname,dpi=150,transparent=False)






    
