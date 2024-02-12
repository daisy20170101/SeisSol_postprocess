#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import scipy.io as sio
import matplotlib.tri as tri
from mpl_toolkits.basemap import Basemap

modelname = 'tp20d'
foldername = 'result4/'

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='geocent', init='EPSG:5936',ellps='WGS84', datum='WGS84')

xdmfFilename =foldername + modelname+'-surface.xdmf'

gpsfolder='GPS/'
stall = np.loadtxt(gpsfolder+'/gnss_station2.txt')
staxyz = pyproj.transform(lla, myproj, stall[:,0],stall[:,1], stall[:,1], radians=False)
stall2 = np.loadtxt('vno_stations2.dat')
staxyz2= pyproj.transform(lla, myproj, stall2[:,1],stall2[:,0], stall2[:,1], radians=False)

# find stations and read records
surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)-1

centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.
Receiver = np.array([staxyz[0],staxyz[1],staxyz[2]])
Receiver = Receiver.transpose()

from scipy import spatial

tree = spatial.KDTree(centers)
dist, ids = tree.query(Receiver)
FidReceiversnew = gpsfolder+'/'+modelname+'/GPS_xyz.txt'
fout = open(FidReceiversnew,'w')
fout1 = open(gpsfolder+'/'+modelname+'/GPS_number.txt','w')

for k in range(0,stall[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()

## read records
sta = np.loadtxt(gpsfolder+modelname+'/GPS_number.txt')
sta = sta[:,0]
nsta = sta.size
vec = np.array([])
xyz = np.array([])

for ista in range(0,nsta):
    uu = LoadData(xdmfFilename,'U',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    vv = LoadData(xdmfFilename,'V',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    ww = LoadData(xdmfFilename,'W',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    slp1 = uu[0][0]
    slp2 = vv[0][0]
    slp3 = ww[0][0]
    vec = np.append(vec,[slp1,slp2,slp3])
    
np.savetxt(gpsfolder+modelname+'/GPS_vec.txt',vec)

## plot mapview of GPS records
coastf = 'coastline/alaska.mat'
coast = sio.loadmat(coastf)


ndt = ReadNdt(xdmfFilename)-1
triang = tri.Triangulation(surfxyz[:,0]/1000,surfxyz[:,1]/1000,connect)

# plot GPS vector

model = np.loadtxt('GPS/'+ modelname +'/GPS_vec.txt')  ;
data = np.loadtxt('GPS/gnss_station2.txt') ;
obv = np.loadtxt('GPS/gnss_data.txt');

#staxyz = pyproj.transform(lla, myproj, data[:,0],data[:,1], radians=False)
ncst = pyproj.transform(lla, myproj, coast['data'][:,0],coast['data'][:,1], radians=False)

obvx = staxyz[0]/1000
obvy = staxyz[1]/1000
#%%
slpz = LoadData(xdmfFilename,'W',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
slpy = LoadData(xdmfFilename,'V',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
slpx = LoadData(xdmfFilename,'U',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)
slp = np.sqrt(slpy[0]*slpy[0]+slpx[0]*slpx[0])
#%%

fig,([ax2,ax3])=plt.subplots(ncols=1,nrows=2,figsize=(5,9.5))

#sc = ax0.tripcolor(triang,td[0]/1e6,cmap='seismic',shading='flat')

sc = ax2.tripcolor(triang,slp,cmap='rainbow',shading='flat',vmin=-4.0,vmax=4.0)
cl = fig.colorbar(sc,ax=ax2)
cl.set_label('horizontal displacement (m)')
#
ax2.set(xlim=(0.90e3, 1.8e3),ylim=(-2.5e3,-1.4e3))
ax2.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)

ax2.quiver(np.append(obvx,1.1e3),np.append(obvy,-2.32e3),np.append(model[0::3]*1000,100),np.append(model[1::3]*1000,0),
           scale=300,scale_units='inches',color='red',headwidth=2,headlength=2) 
     
ax2.quiver(np.append(obvx,1.1e3),np.append(obvy,-2.36e3),np.append(obv[:,2]*1000,100),np.append(obv[:,3]*1000,0),
           scale=300,scale_units='inches',color='orange',headwidth=2,headlength=2) 

ax2.text(1.1e3,-2.3e3,'100 mm')
ax2.text(1.25e3,-2.34e3,'mod')
ax2.text(1.25e3,-2.38e3,'obv')

##     ax2.set_title('Mapview of GPS vector ')

sc = ax3.tripcolor(triang,slpz[0],cmap='rainbow',shading='flat',vmax=4.0,vmin=-4.0)
cl = fig.colorbar(sc,ax=ax3)
cl.set_label('vertical displacement (m)')
##
ax3.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)
ax3.set(xlim=(0.9e3, 1.8e3),ylim=(-2.5e3,-1.4e3))
#
ax3.quiver(np.append(obvx+0.01e3,1.1e3),np.append(obvy,-2.32e3),np.append(model[2::3]-model[2::3],100),np.append(model[2::3]*1000,0),
           scale=300,scale_units='inches',color='red',headwidth=2,headlength=2)
#
ax3.quiver(np.append(obvx,1.1e3),np.append(obvy,-2.36e3),np.append(obv[:,3]-obv[:,3],100),np.append(obv[:,3]*1000,0),
           scale=300,scale_units='inches',color='orange',headwidth=2,headlength=2)
#
ax3.text(1.1e3,-2.3e3,'100 mm')
ax3.text(1.25e3,-2.34e3,'mod')
ax3.text(1.25e3,-2.38e3,'obv')

outname = './'+modelname+'-gps.png'
plt.savefig(outname,dpi=150,transparent=False)





    
