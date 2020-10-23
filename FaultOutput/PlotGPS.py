#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: D. Li
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import matplotlib.tri as tri
from mpl_toolkits.basemap import Basemap

modelname = 'f5'
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

# plot GPS vector

model = np.loadtxt('GPS/'+ modelname +'/GPS_vec.txt')  ;
data = np.loadtxt('GPS/GPS_station2.txt') ;
obv = np.loadtxt('GPS/GPS_data.txt');

dataxyz = pyproj.transform(lla, myproj, -data[:,0],data[:,1],data[:,1], radians=False)

obvx = dataxyz[0]/1000 - refer[0]/1000
obvy = dataxyz[1]/1000 - refer[1]/1000
#%%
#td = LoadData(xdmfFilename,'T_d',connect.shape[0],idt=ndt -1,oneDtMem=True,firstElement=-1)
#pr = LoadData(xdmfFilename,'PSR',connect.shape[0],idt=ndt -1,oneDtMem=True,firstElement=-1)
slp = LoadData(xdmfFilename,'ASl',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)

#srd = LoadData(xdmfFilename,'SRd',connect.shape[0],idt= ndt-1,oneDtMem=True,firstElement=-1)


#%%

fig,ax2=plt.subplots(nrows=1,ncols=1,figsize=(5,4))

#sc = ax0.tripcolor(triang,td[0]/1e6,cmap='seismic',shading='flat')

sc = ax2.tripcolor(triang,slp[0],cmap='viridis',shading='flat')
cl = fig.colorbar(sc,ax=ax2)
cl.set_label('Slip (m)')
#
ax2.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
ax2.set(xlim=( -150, 150),ylim=(-200,100))

#ax2.quiver([dataxyz[0],-110],[dataxyz[1];-180]],[[model[4::3]*1e3;50],[model[5::3]*1e3;0]]) 
ax2.quiver(np.append(obvx,-110),np.append(obvy,-170),np.append(model[0::3]*1000,50),np.append(model[1::3]*1000,0),
           scale=120,scale_units='inches',color='red',headwidth=1,headlength=1) 
     
ax2.quiver(np.append(obvx,-110),np.append(obvy,-180),np.append(obv[:,1]*1000,50),np.append(obv[:,2]*1000,0),
           scale=120,scale_units='inches',color='orange',headwidth=1,headlength=1) 

ax2.text(-130,-140,'50 mm')
ax2.text(-130,-150,'model')
ax2.text(-130,-160,'obv.')

#ax2.set_title('Mapview of Mud')

#sc = ax3.tripcolor(triang,srd[0],cmap='seismic',shading='flat')
#cl = fig.colorbar(sc,ax=ax3)
#cl.set_label('Slip rate (m/s)')
#
#ax3.plot(xtrch[:],ytrch[:],'.k',markersize=0.1)
#ax3.set(xlim=( -150, 150),ylim=(-200,100))

outname = './'+modelname+'-gps.png'
plt.savefig(outname,dpi=150,transparent=False)





    
