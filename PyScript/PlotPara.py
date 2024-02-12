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
import scipy.io as sio

#%%
modelname = 'tp12'
folder = 'result_large/'
xdmfFilename = folder + modelname+'-fault.xdmf'

coastf = 'coastline/alaska.mat'
coast = sio.loadmat(coastf)
hypoll = np.loadtxt('hypocenters.dat')

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='geocent',init='EPSG:5936',ellps='WGS84', datum='WGS84')

#ndt = ReadNdt(xdmfFilename)
xyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)

hypoxyz =  pyproj.transform(lla, myproj,hypoll[:,0],hypoll[:,1],radians=False)
ncst = pyproj.transform(lla, myproj, coast['data'][:,0],coast['data'][:,1], radians=False)
triang = tri.Triangulation(xyz[:,0]/1000,xyz[:,1]/1000,connect)

#%%
td0 = LoadData(xdmfFilename,'Td0',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)
pn0 = LoadData(xdmfFilename,'Pn0',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)
mud0 =  LoadData(xdmfFilename,'Mud',connect.shape[0],idt=0,oneDtMem=True,firstElement=-1)

R   = - td0[0]/pn0[0]-mud0[0]
R0  = - td0[0]/pn0[0]
cfs = -(td0[0]/pn0[0])
s   = (-pn0[0]*mud0[0]-td0[0])/(-mud0[0]*pn0[0]+0.59*pn0[0])

#%%

fig,([ax0,ax1])=plt.subplots(nrows=1,ncols=2,figsize=(9.5,4))

sc = ax0.tripcolor(triang,mud0[0],cmap='plasma',shading='flat',vmin=0.0,vmax=0.6)
cl = fig.colorbar(sc,ax=ax0)
cl.set_label('mu')

ax0.plot(hypoxyz[0]/1e3,hypoxyz[1]/1e3,'*w',markersize=3)
ax0.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)
ax0.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))
#ax0.set_title('Mapview of Td0')

sc = ax1.tripcolor(triang,-pn0[0]/1e6,cmap='plasma',shading='flat',vmin=0,vmax=500)
cl = fig.colorbar(sc,ax=ax1)
cl.set_label('Pn0 (MPa)')

ax1.plot(hypoxyz[0]/1e3,hypoxyz[1]/1e3,'*w',markersize=3)
ax1.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)
ax1.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))
#ax1.set_title('Mapview of Pn0')

outname = modelname+'-para2.png'
plt.savefig(outname,dpi=100,transparent=False)





    
