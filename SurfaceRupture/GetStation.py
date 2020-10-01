#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:06:20 2019

Get nearst piont to the GPS stations from seissol output

@author: dli
"""


from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
from scipy import spatial

# fault trace for surface rupture 
#fault = np.loadtxt('../ruptures.dat')
folder = '/import/deadlock-data/dli/Ridgecrest/Surface/'
fault = np.loadtxt(folder+'fault_trace_Mil.dat')

xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/NewGeometry/output_Mw6471_Plastic_gamma085_dCFS_TR_R07_100s/data-surface.xdmf'
surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.

#%% fault point for fault trace
fault_pos= fault.copy()
fault_pos[:,0] = fault[:,0]+400

tree = spatial.KDTree(centers)
# positive
dist, ids = tree.query(fault_pos)
FidReceiversnew = 'fault2_trace-pos'+'.txt'
fout = open(FidReceiversnew,'w')
fout1 = open('fault2_num-pos'+'.txt','w')

for k in range(0,fault_pos[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec = centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()

# negative
fault_neg = fault.copy()
fault_neg[:,0] = fault[:,0]-400

tree = spatial.KDTree(centers)

dist, ids = tree.query(fault_neg)
FidReceiversnew = 'fault2_trace-neg'+'.txt'
fout = open(FidReceiversnew,'w')
fout1 = open('fault2_num-neg'+'.txt','w')

for k in range(0,fault_neg[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec = centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))
        fout1.write("%d %f\n" %(ids[k],dist[k]))

fout.close()
fout1.close()
