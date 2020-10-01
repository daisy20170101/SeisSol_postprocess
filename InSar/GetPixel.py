#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:06:20 2019

Get nearst piont to the GPS stations from seissol output

@author: dli
"""


#from pythonXdmfReader.pythonXdmfReader import *
import pyproj
import numpy as np

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')
 
#staxyz = np.loadtxt('GPS/GPS_sta.txt')

folder = '/import/deadlock-data/dli/Ridgecrest/GPS/YangHauksson/'

los = np.loadtxt('/import/deadlock-data/dli/Ridgecrest/SV_los_dsamp_dtrend/t71_des_s1.lltnde')

staxyz = los[:,0:3]

xyz = pyproj.transform(lla, myproj, staxyz[:,0],staxyz[:,1], staxyz[:,2], radians=False)

#centers = np.loadtxt('../GPS/YangHauksson/surfxyz_M64.txt')

centers = np.loadtxt(folder+'/surfxyz_M64.txt')
#slp = np.loadtxt('../GPS/YangHauksson/totalslip_M64.txt')
slp = np.loadtxt(folder+'/totalslip_M71.txt')

Receiver = np.array([xyz[0],xyz[1],xyz[2]])

Receiver = Receiver.transpose()

from scipy import spatial

tree = spatial.KDTree(centers)

dist, ids = tree.query(Receiver)

FidReceiversnew = 'InSar_xyz_slp_M64.txt'
FidReceiversnew = 'InSar_xyz_slp_M71.txt'

fout = open(FidReceiversnew,'w')

fout1 = open('InSar_number_M64.txt','w')
fout1 = open('InSar_number_M71.txt','w')

for k in range(0,staxyz[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        slprec=slp[ids[k]]
        fout.write("%f %f %f %f\n" %(newrec[0],newrec[1],newrec[2],slprec))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()
