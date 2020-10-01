# SeisSol_postprocess

To read and plot GPS vectors, use the scripts in GPS/ folder.

1) python GetStaM64.py

Change xdmfFilename to be the surface hdf5 output and staxyz to be the GPS observation data (longitude, latitude, dx,dy)

2) python ReadGPSM64.py

Change xdmfFilename to be the surface hdf5 output 

3) PlotVectorM64.py 

To be able to use these, you need pythonXdmfReader in SeisSol submodules: https://github.com/SeisSol/SeisSol/tree/master/submodules

