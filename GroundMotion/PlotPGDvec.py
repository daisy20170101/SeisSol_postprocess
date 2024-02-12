#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt
import pyproj

fault = np.loadtxt('./ruptures.dat')
fault = fault * 1e-3

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')


surfxyz = np.loadtxt('GroundMotion/VecData_M64.txt')
xyz = pyproj.transform(lla, myproj, surfxyz[:,0],surfxyz[:,1], surfxyz[:,0], radians=False)
x = xyz[0][::1]*1e-3
y = xyz[1][::1]*1e-3

azi = np.arctan2(surfxyz[:,3],surfxyz[:,2])


plt.figure()

plt.subplot(121)

plt.quiver(x,y,surfxyz[:,5]*np.cos(azi),surfxyz[:,5]*np.sin(azi),color='k',lw=2) 
plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)

plt.xlim( [350, 555])
plt.ylim( [3850,4060])
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('M6.4')


surfxyz = np.loadtxt('GroundMotion/VecData_M71.txt')
xyz = pyproj.transform(lla, myproj, surfxyz[:,0],surfxyz[:,1], surfxyz[:,0], radians=False)
x = xyz[0][::10]*1e-3
y = xyz[1][::10]*1e-3
azi = np.arctan2(surfxyz[:,3],surfxyz[:,2])


plt.subplot(122)
plt.quiver(x,y,surfxyz[:,5]*np.cos(azi),surfxyz[:,5]*np.sin(azi),color='k',lw=2) 
plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
plt.xlim( [350, 555])
plt.ylim( [3850,4060])
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('M7.1')

plt.show()




    
