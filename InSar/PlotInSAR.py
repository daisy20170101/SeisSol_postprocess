#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

Plot surface displacements of SeisSol and InSAR records.

@author: D. Li
"""

#from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import pyproj
import matplotlib.pyplot as plt

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')

los = np.loadtxt('/import/deadlock-data/dli/Ridgecrest/SV_los_dsamp_dtrend/t71_des_s1.lltnde')
los_angle = np.array([np.mean(los[:,3]),np.mean(los[:,4]),np.mean(los[:,5])])

xyz = pyproj.transform(lla, myproj, los[:,0],los[:,1], los[:,2], radians=False)

data = los[:,6]

x = xyz[0][:]
y = xyz[1][:]


centers = np.loadtxt('surfxyz_M64.txt')
slp6 = np.loadtxt('totalslip_M64.txt')
slp7 = np.loadtxt('totalslip_M71.txt')

#slp1 = np.loadtxt('InSar_xyz_slp_M64.txt')
slp2 = np.loadtxt('InSar_xyz_slp_M71.txt')
slp = slp2[:,3]

## add fault trace in the plot
modelname = '/import/deadlock-data/dli/Ridgecrest/GPS/'
fault = np.loadtxt(modelname+'../ruptures.dat')
fault = fault * 1e-3

plt.figure(figsize=(6,4))
plt.subplot(121)

sc = plt.scatter(x*1e-3,y*1e-3,s=25,c=data/1000,alpha=0.8,vmin=-1,vmax=1,cmap='RdBu_r')
cl = plt.colorbar(sc)
cl.set_label('LOS (m)')
      
plt.xlim( [400, 500])
plt.ylim( [3925,3980])
plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)

plt.title('InSAR LOS slip (m)')
plt.xlabel('x (km)')
plt.ylabel('y (km)')

plt.subplot(122)

sc = plt.scatter(centers[::4,0]*1e-3,centers[::4,1]*1e-3,s=5,c=slp6[::4]+slp7[::4],alpha=0.8,vmin=-1,vmax=1,cmap='RdBu_r')
cl = plt.colorbar(sc)
cl.set_label('LOS (m)')

      
plt.xlim( [400, 500])
plt.ylim( [3925,3980])
plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)

plt.title('Model: M6.4+M7.1')
plt.xlabel('x (km)')


#plt.subplot(133)
#
#sc = plt.scatter(slp1[:,0]*1e-3,slp1[:,1]*1e-3,s=25,c=(slp-data/1000),alpha=0.8,vmin=-1.0,vmax=1.0,cmap='RdBu_r')
#cl = plt.colorbar(sc)
#cl.set_label('Misfit (m)')
#
##plt.xlim( [350, 555])
##plt.ylim( [3850,4060])
#plt.xlim( [400, 500])
#plt.ylim( [3925,3980])
#plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
#
#plt.title('Model - Data')
#plt.xlabel('x (km)')

plt.savefig("InSAR.png",dpi=150)   





    
