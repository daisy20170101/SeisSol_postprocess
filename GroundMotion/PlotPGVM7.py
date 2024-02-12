#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:28:14 2018

@author: dli
"""

import numpy as np
import matplotlib.pyplot as plt
import pyproj

modelname = 'YangHauksson'
#modelname = 'Hardebeck'

fault = np.loadtxt('../ruptures.dat')
fault = fault * 1e-3

#model = np.loadtxt(modelname+'/GPS_vec_M71.txt')  
#modelxyz = np.loadtxt(modelname+'/GPS_xyz_M71.txt')
#data = np.loadtxt('GPS_M71_data2.txt') 
#length = data.shape[0]
#
#lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
#myproj = pyproj.Proj(proj='utm',zone='11N',ellps='WGS84', datum='WGS84')
#staxyz = pyproj.transform(lla, myproj, data[:,0],data[:,1],data[:,1]-data[:,1], radians=False)


surfxyz = np.loadtxt('../GPS/'+ modelname + '/surfxyz_M71.txt')
slp = np.loadtxt(modelname + '/pgv_M71.txt')

#%%

plt.figure()
#plt.subplot(121)

sc = plt.scatter(surfxyz[::4,0]*1e-3,surfxyz[::4,1]*1e-3,s=0.5,c=slp[::4],alpha=0.8,vmin=-0.8,vmax=0.8,cmap='seismic')
cl = plt.colorbar(sc)
cl.set_label('PGV (m/s)')

plt.quiver(np.append(modelxyz[7:length,0]*1e-3,355),np.append(modelxyz[7:length,1]*1e-3,3905),
           np.append(model[24::3]*1000,120),np.append(model[25::3]*1000,0),scale=200, 
           scale_units='inches',color='orange',headwidth=1,headlength=1) 
      
plt.quiver(np.append(staxyz[0][7:length]*1e-3,355),np.append(staxyz[1][7:length]*1e-3,3895),np.append(data[7:length,2],120),
           np.append(data[7:length,3],0),scale=200, 
           scale_units='inches',color='gray',headwidth=1,headlength=1) 


plt.quiver(np.append(modelxyz[0:7,0]*1e-3,355),np.append(modelxyz[0:7,1]*1e-3,3875),
           np.append(model[[3,6,9,12,15,18,21]]*1000,240),np.append(model[[4,7,10,13,16,19,22]]*1000,0),scale=400, 
           scale_units='inches',color='brown',headwidth=1,headlength=1) 
      
plt.quiver(np.append(staxyz[0][0:7]*1e-3,355),np.append(staxyz[1][0:7]*1e-3,3865),np.append(data[0:7,2],240),
           np.append(data[0:7,3],0),scale=400, 
           scale_units='inches',color='k',headwidth=1,headlength=1) 

plt.xlim( [350, 555])
plt.ylim( [3850,4060])
plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)

plt.title('GPS:Mw7.1 -'+ modelname)

plt.text(355,3915,'240 mm')
plt.text(355,3908,'model')
plt.text(355,3898,'UNAVCO')

plt.text(355,3885,'240 mm')
plt.text(355,3878,'model')
plt.text(355,3868,'UNAVCO')

plt.show()   

### M71
#model = np.loadtxt(modelname+'/GPS_vec_M71.txt')  
#  
#modelxyz = np.loadtxt('GPS_xyz_M71.txt')
#  
#data = np.loadtxt('GPS_M71_data.txt') 
#
#
#lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
#
#myproj = pyproj.Proj(proj='utm',zone='11N',ellps='WGS84', datum='WGS84')
#
#staxyz = pyproj.transform(lla, myproj, data[:,0],data[:,1],data[:,1]-data[:,1], radians=False)
#
#surfxyz = np.loadtxt(modelname + '/surfxyz_M71.txt')
#slp = np.loadtxt(modelname + '/totalslip_M71.txt')
#
##surfxyz = np.loadtxt('GPS/surfxyz_M71.txt')
##slp = np.loadtxt('GPS/totalslip_M71.txt')
#
#plt.subplot(122)
#
#sc = plt.scatter(surfxyz[::8,0]*1e-3,surfxyz[::8,1]*1e-3,s=0.5,c=slp[::8],
#                 alpha=0.8,vmin=-0.8,vmax=0.8,cmap='seismic')
#cl = plt.colorbar(sc)
#cl.set_label('LOS (m)')
#
#plt.quiver(np.append(staxyz[0]*1e-3,355),np.append(staxyz[1]*1e-3,3860),np.append(data[:,2]/10,40),
#           np.append(data[:,3]/10,0),scale=60, 
#           scale_units='inches',color='k') 
#
#plt.quiver(np.append(modelxyz[:,0]*1e-3,355),np.append(modelxyz[:,1]*1e-3,3865),
#           np.append(model[3::3]*100,40),np.append(model[4::3]*100,0),scale=60, 
#           scale_units='inches',color='r')  
#         
#plt.xlim( [350, 555])
#plt.ylim( [3850,4060])
#plt.title('GPS:Mw7.1 -'+ modelname)
#plt.plot(fault[:,0],fault[:,1],'.k',markersize=0.1)
#plt.text(355,3869,'40 cm')


   
    
    

        