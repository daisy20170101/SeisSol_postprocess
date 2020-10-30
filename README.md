# SeisSol_postprocess
## Processing GPS vector records comparison map

To read and plot GPS vectors, use the scripts in GPS/ folder.

1) python GetStaM64.py

Change xdmfFilename to be the surface hdf5 output and staxyz to be the GPS observation data (longitude, latitude, dx,dy)

2) python ReadGPSM64.py

Change xdmfFilename to be the surface hdf5 output 

3) PlotVectorM64.py 

To be able to use these, you need pythonXdmfReader in SeisSol submodules: https://github.com/SeisSol/SeisSol/tree/master/submodules

## Ploting fault output of SeisSol

To read SeisSol's fault out variables, use the scripts in FaultOutput

1) PlotPara.py: plot initial stress (Td0, Pn0), friction coefficient (MuS) and R (Td0/Pn0);
2) PlotSnap.py: plot snapshots of slip rate (m/s) at step 1, ndt/4, ndt/2 ,3/4*ndt;
3) PlotResult.py: plot fault variables (slip rate, slip, rupture speed, and stress drop) at final time step;
