#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:06:20 2019

Get nearst piont to the GPS stations from seissol output

@author: D. li
"""

from pythonXdmfReader.pythonXdmfReader import *
import pyproj
import numpy as np
from scipy import spatial

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

myproj = pyproj.Proj(proj='utm', zone='11N',ellps='WGS84', datum='WGS84')
 
#staxyz = np.loadtxt('GPS/GPS_sta.txt')
#staxyz = np.loadtxt('GPS_M71_data2.txt')
folder = '/import/deadlock-data/dli/Ridgecrest/GPS/'
#folder = sys.argv[1]

staxyz = np.loadtxt(folder+'GPS_M64_data2.txt')
     
xyz = pyproj.transform(lla, myproj, staxyz[:,0],staxyz[:,1], staxyz[:,1], radians=False)

xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/NewGeometry/output_Mw6471_Plastic_gamma085_dCFS_TR_R07_100s/data-surface.xdmf'
#xdmfFilename =  sys.argv[1]

surfxyz = ReadGeometry(xdmfFilename)

connect = ReadConnect(xdmfFilename)

centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.

Receiver = np.array([xyz[0],xyz[1],xyz[2]])

Receiver = Receiver.transpose()

tree = spatial.KDTree(centers)

dist, ids = tree.query(Receiver)

FidReceiversnew = 'GPS_xyz_M64.txt'

fout = open(FidReceiversnew,'w')

fout1 = open('GPS_number_M64.txt','w')

for k in range(0,staxyz[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()
