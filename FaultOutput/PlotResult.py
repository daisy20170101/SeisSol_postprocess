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
asl= LoadData(xdmfFilename,'ASl',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
vr =LoadData(xdmfFilename,'Vr',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
td = LoadData(xdmfFilename,'T_d',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
srd=LoadData(xdmfFilename,'SRd',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)

#%%

fig,([ax0,ax1],[ax2,ax3])=plt.subplots(nrows=2,ncols=2,figsize=(8,6))

sc = ax0.tripcolor(triang,srd[0],cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax0)
cl.set_label('slip rate (m/s)')

ax0.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax0.plot(c20[:,0],c20[:,1],'.k',markersize=0.1)
#ax0.plot(c40[:,0],c40[:,1],'.k',markersize=0.1)
#ax0.plot(c60[:,0],c60[:,1],'.k',markersize=0.1)
#ax0.plot(c80[:,0],c80[:,1],'.k',markersize=0.1)
#plt.plot(c5[:,0],c5[:,1],'-k',markersize=0.1)

ax0.set(xlim=( -150, 150),ylim=(-200,100))
#ax0.set_title('Mapview of Td0')

sc = ax1.tripcolor(triang,asl[0],cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax1)
cl.set_label('slip m')

ax1.set(xlim=(-150, 150),ylim=(-200,100))
ax1.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)

#ax1.set_title('Mapview of Mud')

sc = ax2.tripcolor(triang,vr[0],cmap='viridis',shading='flat',vmin=0.0,vmax=3400.0)
cl = fig.colorbar(sc,ax=ax2)
cl.set_label('Vr m/s')

ax2.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
ax2.set(xlim=( -150, 150),ylim=(-200,100))

#ax2.set_title('Mapview of Mud')

sc = ax3.tripcolor(triang,td[0]/1e6,cmap='seismic',shading='flat',vmin=0,vmax=1)
cl = fig.colorbar(sc,ax=ax3)
cl.set_label('Td MPa')

ax3.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
ax3.set(xlim=( -150, 150),ylim=(-200,100))


outname = modelname+'-result.png'
plt.savefig(outname,dpi=150,transparent=False)






    
