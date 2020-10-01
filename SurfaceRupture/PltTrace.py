#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:35:54 2020

@author: dli
"""

import numpy as np
import matplotlib.pyplot as plt
import pyproj

pi = np.pi

folder = '/import/deadlock-data/dli/Ridgecrest/Surface/'
obv1 =np.loadtxt(folder+'PL_slip_profile.txt')
obv2 =np.loadtxt(folder+'S2_slip_profile.txt')


fault21_disp =  np.loadtxt(folder+'fault2_disp-pos.txt')
fault2_trace =  np.loadtxt(folder+'fault_trace_Mil.dat')
fault22_disp =  np.loadtxt(folder+'fault2_disp-neg.txt')

fault2_disp = fault21_disp - fault22_disp

#fault_disp = np.loadtxt('fault2_disp.txt')
#fault_trace =np.loadtxt('fault2_trace.txt')

hypo = np.array([-117.599, 35.770])

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')
hypoxyz = pyproj.transform(lla, myproj, hypo[0],hypo[1], hypo[1], radians=False)


theta = 38 /180 * np.pi

plt.figure()

plt.plot(-fault2_trace[:,1]/1e3/np.cos(38/180*pi)+hypoxyz[1]/1e3/np.cos(38/180*pi),
        fault2_disp[:,0]*np.sin(theta) - fault2_disp[:,1]*np.cos(theta),'-k')

plt.plot(-obv1[:,0]+obv1[17,0],-obv1[:,1],'-r')
plt.plot(-obv2[:,0]+obv2[22,0],-obv2[:,1],'-b')

#plt.plot(rupt[:,0],rupt[:,1],'.k',markersize=0.1)
#plt.plot(fault2[:,0],fault2[:,1],'-r')
##plt.plot(fault1[:,0],fault1[:,1],'-b')
#plt.plot(fault4[:,0],fault4[:,1],'-g')
plt.xlabel('Distance from epicenter (km)')
plt.ylabel('fault parallel displacement (m)')
plt.legend(['This model','PL-Milliners','S2-Milliners'])

plt.savefig("Surf_offset.png",dpi=300)   


