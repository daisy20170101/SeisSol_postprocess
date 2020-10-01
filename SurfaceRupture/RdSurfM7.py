#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np


xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/NewGeometry/output_Mw6471_Plastic_gamma085_dCFS_TR_R07_100s/data-surface.xdmf'

ndt = ReadNdt(xdmfFilename)

#direction = pos
direction = 'pos'

sta = np.loadtxt('fault2_num-'+direction+'.txt')
sta = sta[:,0]
nsta = sta.size
vec = np.zeros((nsta,3))
xyz = np.zeros((nsta,3))

for ista in range(0,nsta):
    
    uu = LoadData(xdmfFilename,'U',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    uu0 =LoadData(xdmfFilename,'U',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    vv = LoadData(xdmfFilename,'V',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    vv0 =LoadData(xdmfFilename,'V',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    ww = LoadData(xdmfFilename,'W',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    ww0 =LoadData(xdmfFilename,'W',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    
    slp1 = uu[0][0] - uu0[0][0]
    slp2 = vv[0][0] - vv0[0][0]  
    slp3 = ww[0][0] - ww0[0][0]
    
    vec[ista,:] = [slp1,slp2,slp3]
    
np.savetxt('fault2_disp-'+direction+'.txt',vec)
    
# direction = negative

direction = 'neg'

sta = np.loadtxt('fault2_num-'+direction+'.txt')
sta = sta[:,0]
nsta = sta.size
vec = np.zeros((nsta,3))
xyz = np.zeros((nsta,3))

for ista in range(0,nsta):
    
    uu = LoadData(xdmfFilename,'U',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    uu0 =LoadData(xdmfFilename,'U',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    vv = LoadData(xdmfFilename,'V',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    vv0 =LoadData(xdmfFilename,'V',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    ww = LoadData(xdmfFilename,'W',1,idt=ndt-1,oneDtMem=True,firstElement=np.int(sta[ista])) 
    ww0 =LoadData(xdmfFilename,'W',1,idt=20,oneDtMem=True,firstElement=np.int(sta[ista]))
    
    slp1 = uu[0][0] - uu0[0][0]
    slp2 = vv[0][0] - vv0[0][0]  
    slp3 = ww[0][0] - ww0[0][0]
    
    vec[ista,:] = [slp1,slp2,slp3]
    
np.savetxt('fault2_disp-'+direction+'.txt',vec)
