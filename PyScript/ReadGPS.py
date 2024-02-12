#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np

#model='s42'

#xdmfFilename='/import/schreck-data/dli/Mexico/Launch_seissol/smallslab/shallowpatch/'+model+'-surface.xdmf'

model='a1'
foldername = 'result2/'
xdmfFilename='./'+foldername +model+'-surface.xdmf'

gpsfolder='GPS/'

ndt = ReadNdt(xdmfFilename)-1
#ndt = 120

sta = np.loadtxt(gpsfolder+model+'/GPS_number.txt')
sta = sta[:,0]
nsta = sta.size

vec = np.array([])
xyz = np.array([])

for ista in range(0,nsta):
    
    uu = LoadData(xdmfFilename,'U',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    vv = LoadData(xdmfFilename,'V',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    ww = LoadData(xdmfFilename,'W',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista]))
    
    slp1 = uu[0][0]
    slp2 = vv[0][0]
    slp3 = ww[0][0]
    
    vec = np.append(vec,[slp1,slp2,slp3])
    
np.savetxt(gpsfolder+model+'/GPS_vec.txt',vec)
    
#    fout ='./gps_sta'+str(ista)+'_U.txt'
#    np.savetxt(fout,slp1)
#    fout ='./gps_sta'+str(ista)+'_V.txt'
#    np.savetxt(fout,slp2)
#    fout ='./gps_sta'+str(ista)+'_W.txt'
#    np.savetxt(fout,slp3)


