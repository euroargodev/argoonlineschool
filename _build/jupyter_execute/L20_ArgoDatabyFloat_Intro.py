#!/usr/bin/env python
# coding: utf-8

# # Accesing Argo data by float

# **Real Time and Calibrated data**
# 
# Since the target is to have the Argo data available within 24 hours of their transmission from the float, this data is called *Real Time* (RT) data.  One year after the data were observed it is, if necessary, adjusted and made public, this data is called *Delayed Mode* (DM). We will begin by focusing in the real time data, and in section [Adjusted data](https://euroargodev.github.io/argoonlineschool/L50_AdjustedData.html) we will describe how the data is adjusted.

# **Data files organized by float**
# 
# <img src="https://github.com/euroargodev/argoonlineschool/raw/master/images/dac.png" alt="xarray logo" width="650"/>

# When accessing the **dac** folder in any of the *FTP* or *HTTP* sites of any of the two GDACs you will find several (11) folders, one for each of the DACs.  Within each one of these folder there is one folder for each one of the floats processed by this particular *DAC*. 
# 
# In the example here, we will use data from float with **WMO** number 6901254, that is proceesed by coriolis (later we will see how to find the DAC for each float), therefore within the folder `./6901254`, we find the following files and folder:
# 
# - 6901254_Rtraj.nc 
# - 6901254_meta.nc  
# - 6901254_prof.nc  
# - 6901254_tech.nc  
# - ./profiles
# 
# we will describe the content of each of these files later, but let's focus on the folder `./profiles/` since it contains one file for each one of the hydrographic cycles carried out by the float. **R6901254_001.nc** is the file that contains the data from the first cycle. It begins with a *R* since it is the real time data, if it began with an *D* it would be adjusted data, or Delayed Mode data; we will see and example in section [**ACTUALIZAR**]. 
# 
# Additionally some argo floats, as 6901254, also made obserations in the first descent from the surface to the parking depth, in this case the name of the files with this data would be **R6901254_001D.nc**.  
# 
# In general, the format of the file names for individual profiles are `<R/D><FloatWmoID>_<XXX><D>.nc` where :
# 
# - The initial *R* indicates Real-Time data, the initial *D* indicates Delayed-Mode data
# - *XXX* is the cycle number
# - The second *D* indicates a descending profile, if exist, while profiles without this D are collected during ascent.
# 
# 
# Note that it may happens that, in the future, you try to downdload the fles from float 6901254 and there is not `R6901254_001.nc` and `R6901254_001D.nc` files, but you find `D6901254_001.nc` and `D6901254_001D.nc` since the R-files are substituded by the D-files once the data is adjusted, we will describe that in detail in section [**ACTUALIZAR**]

# >The data from the float is pre-downloaded in the *./Data* folder, but you can dowload it from the Coriolis GDAC. See the [Data](https://euroargodev.github.io/argoonlineschool/README.html#data) section for instructions on how to download the data.
# 
# 
