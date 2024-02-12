#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

#from pythonXdmfReader.pythonXdmfReader import *
import numpy as np

#xdmfFilename='/import/freenas-m-05-seissol/Ridgecrest/Hardebeck_RS/Mw71_Hardebeck_R07_Gamma085/f200_o4_cvmh1000m_andersonian_Mw71_Plastic/data-surface.xdmf'
#xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/A4B4/f200_o4_cvmh1000m_andersonian_Mw71_Plastic_gamma_085/data-surface.xdmf'
#xdmfFilename = '/import/deadlock-data/dli/Ridgecrest/f200_o4_cvmh1000m_andersonian_Mw64_Plastic_gamma_085_6km/dat-surface.xdmf'
#xdmfFilename = '/import/freenas-m-05-seissol/Ridgecrest/Output_Files/A4B4_100s/Flat_Seismogenic_Depth/f200_o4_cvmh1000m_andersonian_Mw64_Plastic_gamma_085/data-surface.xdmf'
#xdmfFilename='/import/freenas-m-05-seissol/Ridgecrest/Output_Files/A4B4_100s/Varied_Seismogenic_Depth/f200_o4_cvmh1000m_andersonian_Mw64_Plastic_gamma_085/data-surface.xdmf'
#xdmfFilename='/import/freenas-m-05-seissol/Ridgecrest/Output_Files/Varied_Seismogenic_Depth_VelStr/data-surface.xdmf'

#xdmfFilename='/import/freenas-m-05-seissol/project/YangHauksson_RS/Mw64_YangHauksson_R07_Gamma085/f200_o4_cvmh1000m_andersonian_Mw64_Plastic/data-surface.xdmf'
#xdmfFilename='/import/freenas-m-05-seissol/project/YangHauksson_RS/Mw71_YangHauksson_R07_Gamma085/f200_o4_cvmh1000m_andersonian_Mw71_Plastic/data-surface.xdmf'
#xdmfFilename='/import/deadlock-data/dli/Ridgecrest/A4B4_AGU/testRadius-surface.xdmf'
#xdmfFilename='/import/freenas-m-05-seissol/Ridgecrest/Output_Files/AGU/output_Mw6471_Plastic_gamma_085_a7_dCFS_TR/data-surface.xdmf'
xdmfFilename='/import/freenas-m-05-seissol/Ridgecrest/Output_Files/AGU/output_Mw6471_Plastic_gamma_085_a7_dCFS_TR_NEW_2/data-surface.xdmf'

#los = np.loadtxt('../SV_los_dsamp_dtrend/t71_des_s1.lltnde')
#
#los_angle = np.array([np.mean(los[:,3]),np.mean(los[:,4]),np.mean(los[:,5])])

ndt = ReadNdt(xdmfFilename)

xyz = ReadGeometry(xdmfFilename)

connect = ReadConnect(xdmfFilename)

centers = (xyz[connect[:,0]] + xyz[connect[:,1]] + xyz[connect[:,2]])/3.

uu = LoadData(xdmfFilename,'U',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
uu0 = LoadData(xdmfFilename,'U',connect.size,idt=100,oneDtMem=True,firstElement=-1)

vv = LoadData(xdmfFilename,'V',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
vv0= LoadData(xdmfFilename,'V',connect.size,idt=100,oneDtMem=True,firstElement=-1)

ww = LoadData(xdmfFilename,'W',connect.size,idt=ndt-1,oneDtMem=True,firstElement=-1)
ww0 =LoadData(xdmfFilename,'W',connect.size,idt=100,oneDtMem=True,firstElement=-1)

slp1 = uu[0][:]- uu0[0][:]
slp2 = vv[0][:]- vv0[0][:]
slp3 = ww[0][:]- ww0[0][:]

slp = slp1*slp1+ slp2*slp2 + slp3*slp3

#fout ='./totalslip'+'_U.txt'
#np.savetxt(fout,slp1)
#
#fout ='./totalslip'+'_V.txt'
#np.savetxt(fout,slp2)
#
#fout ='./totalslip'+'_W.txt'
#np.savetxt(fout,slp3)

fout ='pgv_M71.txt'

np.savetxt(fout,slp)

#np.savetxt('YangHauksson/surfxyz_M71.txt',centers)




    
