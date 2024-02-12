#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:06:20 2019

Get nearst piont to the GPS stations from seissol output

@author: dli
"""


from pythonXdmfReader.pythonXdmfReader import *
import pyproj
import numpy as np

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

myproj = pyproj.Proj(proj='geocent', init='EPSG:5936',ellps='WGS84', datum='WGS84')

#model = 's21' 
model = 'a1'
foldername = 'result2/'

#staxyz = np.loadtxt('GPS/GPS_sta.txt')
#staxyz = np.loadtxt('GPS_sta_M64.txt')
gpsfolder='GPS/'
staxyz = np.loadtxt(gpsfolder+'/gnss_station2.txt')

     
xyz = pyproj.transform(lla, myproj, staxyz[:,0],staxyz[:,1], staxyz[:,1], radians=False)

#xdmfFilename='/import/schreck-data/dli/Mexico/Launch_seissol/smallslab/shallowpatch/'+model+'-surface.xdmf'
xdmfFilename='./'+foldername +model+'-surface.xdmf'

surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.
Receiver = np.array([xyz[0],xyz[1],xyz[2]])

Receiver = Receiver.transpose()

from scipy import spatial

tree = spatial.KDTree(centers)

dist, ids = tree.query(Receiver)

FidReceiversnew = gpsfolder+'/'+model+'/GPS_xyz.txt'

fout = open(FidReceiversnew,'w')

fout1 = open(gpsfolder+'/'+model+'/GPS_number.txt','w')

for k in range(0,staxyz[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()
