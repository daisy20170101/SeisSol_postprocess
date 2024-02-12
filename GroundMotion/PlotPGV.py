#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt
import pyproj

fault = np.loadtxt('./ruptures.dat') # fault trace
fault = fault*1e-3

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')

#surfxyz = np.loadtxt('GroundMotion/StrongMotion_M64.txt')
surfxyz = np.loadtxt('GroundMotion/grid.xyz.M71/grid.dat',comments='#',skiprows=2)
stadata = np.loadtxt('GroundMotion/station_M7.dat')

#surfxyz = np.loadtxt('GroundMotion/grid.xyz.M64/grid.dat',comments='#')
#stadata = np.loadtxt('GroundMotion/station_M6.dat',delimiter=',')

xyz = pyproj.transform(lla, myproj, surfxyz[:,0],surfxyz[:,1], surfxyz[:,0], radians=False)
staxyz = pyproj.transform(lla, myproj, stadata[:,1],stadata[:,0], stadata[:,0], radians=False)


#%%
x = xyz[0][::5]*1e-3
y = xyz[1][::5]*1e-3

plt.figure()

#plt.subplot(121)
sc = plt.scatter(x,y,c=surfxyz[::5,3]/100,cmap='rainbow',vmin=0,vmax=0.7)
plt.scatter(staxyz[0]/1e3,staxyz[1]/1e3,c=stadata[:,4]/100,cmap='rainbow',edgecolors='none',marker='^',vmin=0,vmax=0.7)

plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
cl = plt.colorbar(sc)
cl.set_label('PGV (m/s)')
plt.xlim( [350, 555])
plt.ylim( [3850,4060])
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('M7.1 - USGS')

#plt.figure()
#
#plt.subplot(121)
#sc = plt.scatter(x,y,c=surfxyz[::5,4],cmap='rainbow',vmin=0,vmax=9)
#plt.scatter(staxyz[0]/1e3,staxyz[1]/1e3,c=stadata[:,3],cmap='rainbow',marker='^',vmin=0,vmax=9)
#
#plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
#cl = plt.colorbar(sc)
#cl.set_label('Intensity')
#plt.xlim( [350, 555])
#plt.ylim( [3850,4060])
#plt.xlabel('x (km)')
#plt.ylabel('y (km)')
#plt.title('M7.1')
#
#
##surfxyz = np.loadtxt('GroundMotion/StrongMotion_M71.txt')
##xyz = pyproj.transform(lla, myproj, surfxyz[:,0],surfxyz[:,1], surfxyz[:,0], radians=False)
##x = xyz[0][::10]*1e-3
##y = xyz[1][::10]*1e-3
#
#
#plt.subplot(122)
#sc = plt.scatter(x,y,c=surfxyz[::5,2],cmap='rainbow',vmin=0,vmax=70)
#plt.scatter(staxyz[0]/1e3,staxyz[1]/1e3,c=stadata[:,5],cmap='rainbow',marker='^')
#
#plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
#cl = plt.colorbar(sc)
#cl.set_label('PGA (%g)')
#plt.xlim( [350, 555])
#plt.ylim( [3850,4060])
#plt.xlabel('x (km)')
#plt.ylabel('y (km)')
#plt.title('M7.1')

plt.show()




    
