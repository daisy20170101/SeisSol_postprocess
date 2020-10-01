#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:28:14 2018
@author: D. li
"""

import numpy as np
import matplotlib.pyplot as plt
import pyproj

modelname = '/import/deadlock-data/dli/Ridgecrest/GPS/'

fault = np.loadtxt(modelname+'../ruptures.dat')
fault = fault * 1e-3

model = np.loadtxt('GPS_vec_M64.txt')  
modelxyz = np.loadtxt('GPS_xyz_M64.txt')
data = np.loadtxt(modelname+'GPS_M64_data2.txt') 
length = data.shape[0]

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm',zone='11N',ellps='WGS84', datum='WGS84')
staxyz = pyproj.transform(lla, myproj, data[:,0],data[:,1],data[:,1]-data[:,1], radians=False)


# add backgroud color of surface slip if necessary
# surfxyz = np.loadtxt( modelname +'surfxyz_M64.txt')
# slp = np.loadtxt(modelname + 'totalslip_M64.txt')


plt.figure()

#sc = plt.scatter(surfxyz[::4,0]*1e-3,surfxyz[::4,1]*1e-3,s=0.5,c=slp[::4],alpha=0.8,vmin=-0.1,vmax=0.1,cmap='RdBu_r')
#cl = plt.colorbar(sc)
#cl.set_label('LOS (m)')

plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)


plt.quiver(np.append(modelxyz[1:length,0]*1e-3,355),np.append(modelxyz[1:length,1]*1e-3,3905),
           np.append(model[6::3]*1000,40),np.append(model[7::3]*1000,0),scale=40, 
           scale_units='inches',color='orange',headwidth=1,headlength=1) 
      
plt.quiver(np.append(staxyz[0][1:length]*1e-3,355),np.append(staxyz[1][1:length]*1e-3,3895),np.append(data[1:length,2],40),
           np.append(data[1:length,3],0),scale=40, 
           scale_units='inches',color='gray',headwidth=1,headlength=1) 

plt.quiver(np.append(modelxyz[0,0]*1e-3,355),np.append(modelxyz[0,1]*1e-3,3875),
           np.append(model[3]*1000,80),np.append(model[4]*1000,0),scale=90, 
           scale_units='inches',color='brown',headwidth=1,headlength=1) 
      
plt.quiver(np.append(staxyz[0][0]*1e-3,355),np.append(staxyz[1][0]*1e-3,3865),np.append(data[0,2],80),
           np.append(data[0,3],0),scale=90, 
           scale_units='inches',color='k',headwidth=1,headlength=1) 

plt.xlim( [350, 555])
plt.ylim( [3850,4060])

plt.title('GPS:Mw6.4')

plt.text(355,3915,'40 mm')
plt.text(355,3908,'model')
plt.text(355,3898,'UNAVCO')

plt.text(355,3885,'80 mm')
plt.text(355,3878,'model')
plt.text(355,3868,'UNAVCO')


plt.savefig("M64_R07_new.png",dpi=300,transparent=False)



   
    
    

        
