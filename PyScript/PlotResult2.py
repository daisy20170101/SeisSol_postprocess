#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: D. Li 
"""
from pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import pyproj
import h5py
import scipy.io as sio

#%%
modelname = 'tp50b'
folder = 'result4/'

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
asl= LoadData(xdmfFilename,'ASl',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
vr =LoadData(xdmfFilename,'Vr',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
#td = LoadData(xdmfFilename,'T_d',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
#srd=LoadData(xdmfFilename,'PSR',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
#pf = LoadData(xdmfFilename,'P_f',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
#tmp = LoadData(xdmfFilename,'Tmp',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
#%%

fig,([ax0,ax1])=plt.subplots(nrows=1,ncols=2,figsize=(9,3.5))


#ax0.set_title('Mapview of Td0')
ax0.plot(hypoxyz[0]/1e3,hypoxyz[1]/1e3,'*w',markersize=3)
ax0.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)
ax0.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))

sc = ax0.tripcolor(triang,asl[0],cmap='plasma',shading='flat',vmin=0.0,vmax=10.0)
cl = fig.colorbar(sc,ax=ax0)
cl.set_label('slip (m)')

ax1.plot(hypoxyz[0]/1e3,hypoxyz[1]/1e3,'*w',markersize=3)
ax1.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)
ax1.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))
#ax1.set_title('Mapview of Mud')

sc = ax1.tripcolor(triang,vr[0],cmap='viridis',shading='flat',vmin=0.0,vmax=3500.0)
cl = fig.colorbar(sc,ax=ax1)
cl.set_label('peak slip rate (m/s)')

#ax2.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax2.set(xlim=( -150, 150),ylim=(-200,100))
#
##ax2.set_title('Mapview of Mud')
#
#sc = ax3.tripcolor(triang,td[0]/pn[0],cmap='seismic',shading='flat',vmin=0,vmax=1)
#cl = fig.colorbar(sc,ax=ax3)
#cl.set_label('Td/Pn ratio')
#
#ax3.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax3.set(xlim=( -150, 150),ylim=(-200,100))

outname = modelname+'-slp-sr.png'
plt.savefig(outname,dpi=100,transparent=False)






    
