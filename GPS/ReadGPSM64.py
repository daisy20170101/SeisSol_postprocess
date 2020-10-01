#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: D. Li 
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np

xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/NewGeometry/output_Mw6471_Plastic_gamma085_dCFS_TR_R07_100s/data-surface.xdmf'

#ndt = ReadNdt(xdmfFilename)
ndt = 20

sta = np.loadtxt('GPS_number_M64.txt')
sta = sta[:,0]
nsta = sta.size

vec = np.array([0,0,0])
xyz = np.array([0,0,0])

for ista in range(0,nsta):
    
    uu = LoadData(xdmfFilename,'U',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    vv = LoadData(xdmfFilename,'V',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    ww = LoadData(xdmfFilename,'W',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    
    slp1 = uu[0][0]
    slp2 = vv[0][0]
    slp3 = ww[0][0]
    
    vec = np.append(vec,[slp1,slp2,slp3])
    
np.savetxt('GPS_vec_M64.txt',vec)
    
#    fout ='./gps_sta'+str(ista)+'_U.txt'
#    np.savetxt(fout,slp1)
#    fout ='./gps_sta'+str(ista)+'_V.txt'
#    np.savetxt(fout,slp2)
#    fout ='./gps_sta'+str(ista)+'_W.txt'
#    np.savetxt(fout,slp3)


