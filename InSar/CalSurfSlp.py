#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: D. Li
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np

xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/NewGeometry/output_Mw6471_Plastic_gamma085_dCFS_TR_R07_100s/data-surface.xdmf'

los = np.loadtxt('/import/deadlock-data/dli/Ridgecrest/SV_los_dsamp_dtrend/t71_des_s1.lltnde')

los_angle = np.array([np.mean(los[:,3]),np.mean(los[:,4]),np.mean(los[:,5])])

ndt = ReadNdt(xdmfFilename)

xyz = ReadGeometry(xdmfFilename)

connect = ReadConnect(xdmfFilename)

centers = (xyz[connect[:,0]] + xyz[connect[:,1]] + xyz[connect[:,2]])/3.

uu = LoadData(xdmfFilename,'U',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
uu0 = LoadData(xdmfFilename,'U',connect.size,idt=20,oneDtMem=True,firstElement=-1)

vv = LoadData(xdmfFilename,'V',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
vv0= LoadData(xdmfFilename,'V',connect.size,idt=20,oneDtMem=True,firstElement=-1)

ww = LoadData(xdmfFilename,'W',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
ww0 =LoadData(xdmfFilename,'W',connect.size,idt=20,oneDtMem=True,firstElement=-1)

slp1 = uu[0][:]- uu0[0][:]
slp2 = vv[0][:]- vv0[0][:]
slp3 = ww[0][:]- ww0[0][:]

slp = slp1*los_angle[0]+ slp2*los_angle[1] + slp3*los_angle[2] 

slp1 = uu0[0][:]
slp2 = vv0[0][:]
slp3 = ww0[0][:]

slp0 = slp1*los_angle[0]+ slp2*los_angle[1] + slp3*los_angle[2] 

#fout ='./totalslip'+'_U.txt'
#np.savetxt(fout,slp1)
#
#fout ='./totalslip'+'_V.txt'
#np.savetxt(fout,slp2)
#
#fout ='./totalslip'+'_W.txt'
#np.savetxt(fout,slp3)

fout ='totalslip_M71.txt'

np.savetxt(fout,slp)

fout ='totalslip_M64.txt'

np.savetxt(fout,slp0)

np.savetxt('surfxyz_M64.txt',centers)




    
