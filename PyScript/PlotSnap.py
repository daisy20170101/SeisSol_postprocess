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
import h5py
import scipy.io as sio

#%%
modelname = 'tp20'
folder = 'result2/'

xdmfFilename = folder + modelname+'-fault.xdmf'

coastf = 'coastline/alaska.mat'
coast = sio.loadmat(coastf)
hypoll = np.loadtxt('hypocenters.dat')

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='geocent',init='EPSG:5936',ellps='WGS84', datum='WGS84')

ndt = ReadNdt(xdmfFilename)-1
xyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)

ncst = pyproj.transform(lla, myproj, coast['data'][:,0],coast['data'][:,1], radians=False)
hypoxyz =  pyproj.transform(lla, myproj,hypoll[:,0],hypoll[:,1],radians=False)

triang = tri.Triangulation(xyz[:,0]/1000,xyz[:,1]/1000,connect)

#%%
srd1= LoadData(xdmfFilename,'SRd',connect.shape[0],idt=int(ndt/4),oneDtMem=True,firstElement=-1)
srd2 =LoadData(xdmfFilename,'SRd',connect.shape[0],idt=int(ndt/2),oneDtMem=True,firstElement=-1)
srd3 = LoadData(xdmfFilename,'SRd',connect.shape[0],idt=int(ndt*3/4),oneDtMem=True,firstElement=-1)
srd4=LoadData(xdmfFilename,'SRd',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)

#%%
fig,([ax0,ax1],[ax2,ax3])=plt.subplots(nrows=2,ncols=2,figsize=(8,6))

sc = ax0.tripcolor(triang,srd1[0],cmap='plasma',shading='flat',vmin=0,vmax=2)
cl = fig.colorbar(sc,ax=ax0)


#ax0.set(xlim=( -150, 150),ylim=(-200,100))
#ax0.set_title('Mapview of Td0')dd

sc = ax1.tripcolor(triang,srd2[0],cmap='plasma',shading='flat',vmin=0,vmax=2)
cl = fig.colorbar(sc,ax=ax1)

#ax1.set(xlim=(-150, 150),ylim=(-200,100))
#ax1.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)

#ax1.set_title('Mapview of Mud')

sc = ax2.tripcolor(triang,srd3[0],cmap='plasma',shading='flat',vmin=0.0,vmax=2.0)
cl = fig.colorbar(sc,ax=ax2)

#ax2.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax2.set(xlim=( -150, 150),ylim=(-200,100))

#ax2.set_title('Mapview of Mud')

sc = ax3.tripcolor(triang,srd4[0],cmap='plasma',shading='flat',vmin=0,vmax=2.0)
cl = fig.colorbar(sc,ax=ax3)
cl.set_label('slip rate m/s')

#ax3.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax3.set(xlim=( -150, 150),ylim=(-200,100))

outname = modelname+'-snap.png'
plt.savefig(outname,dpi=100,transparent=False)
