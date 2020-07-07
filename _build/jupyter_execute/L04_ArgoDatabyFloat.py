# Argo data by float

## Data files organized by float

<img src="https://github.com/euroargodev/argoonlineschool/raw/master/images/dac.png" alt="xarray logo" width="650"/>

Accessing the dac folder in any of the *FTP* or *HTTP* sites of any of the two GDACs you will find several (11) folders, one for each of the DACs.  Within each one of these folder there is one folder for each one of the floats processed by this particular *DAC*. In the first example here, we will use data from float with **WMO** number 6901254, that is proceesed by coriolis (later we will see how to find the DAC for each float). Within the folder `./6901254`, we find the following files:

- 6901254_Rtraj.nc 
- 6901254_meta.nc  
- 6901254_prof.nc  
- 6901254_tech.nc  

we will describe the content of each of these files later, but let's focus on the folder `./profiles/` since it contains one file for each one of the hydrographic profiles measured by the float. **R6901254_001.nc** is the file that contains the data from the first profiles. It begins with a *R* since it is the real time data, if it began with an *D* it would be adjusted data, or Delayed Mode data; we will see and example in section [**ACTUALIZAR**]. 

Additionally some argo floats, as 6901254, also made obserations in the first descent from the surface to the parking depth, in this case the name of the files with this profile would be **R6901254_001D.nc**.  

In summary, the format of the file names for individual profiles are `<R/D><FloatWmoID>_<XXX><D>.nc` where :

- The initial *R* indicates Real-Time data, the initial *D* indicates Delayed-Mode data
- *XXX* is the cycle number
- The second *D* indicates a descending profile, if exist, while profiles without this D are collected during ascent.


Note that it may happens that, in the future, you try to downdload the fles from float 6901254 and there is not `R6901254_001.nc` and `R6901254_001D.nc` files, but you find `D6901254_001.nc` and `D6901254_001D.nc` since the R-files are substituded by the D-files once the data is adjusted, we will describe that in detail in section [**ACTUALIZAR**]

>The data from the float is pre-downloaded in the *./Data* folder, but you can dowload it from the Coriolis GDAC. See the [Data](https://euroargodev.github.io/argoonlineschool/README.html#data) section for instructions on how to download the data.



## Reading an Argo profile - the building blocks of Argo

#First, import libraries
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
%matplotlib inline

Prof1 = xr.open_dataset('./Data/6901254/profiles/R6901254_001.nc')
Prof1D = xr.open_dataset('./Data/6901254/profiles/R6901254_001D.nc')

Prof1 

Profile1D = xr.open_dataset('./Data/6901254/profiles/R6901254_001D.nc')
print(Profile1.VERTICAL_SAMPLING_SCHEME.values[1])
l=Profile1.DATA_CENTRE[0].values
type(l)

Once a floats is deployed...

#print(Profile1.PSAL)
print(Profile1D.DIRECTION)
print(Profile1D.CYCLE_NUMBER, Profile1.CYCLE_NUMBER,Profile10.CYCLE_NUMBER)

fig, ax = plt.subplots(1,2,figsize=(8,8))
ax[0].plot(Profile1.PSAL,-Profile1.PRES,'bo')
ax[0].grid()

ax[1].plot(Profile1.TEMP,-Profile1.PRES,'bo')
ax[1].grid()



hablar sobre ptem...

xrDS1D = xr.open_dataset('./Data/6901254/profiles/R6901254_001D.nc')
print(xrDS1D.JULD.values[0])


from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()
argo_loader = ArgoDataFetcher(backend='erddap')
argo_loader = ArgoDataFetcher(cachedir='tmp')

apDS=argo_loader.float(6901255).to_xarray()

apDS2=argo_loader.profile(6901255,1).to_xarray()

apDS2.argo.point2profile()

The core-Argo profile files contain the core parameters provided by a float: pressure, temperature, salinity, conductivity (PRES, TEMP, PSAL, CNDC). All additional parameters are managed in B-Argo data files (see §0).   

## Meta data





## Trayectory data

Rtraj = xr.open_dataset('./Data/6901254/6901254_Rtraj.nc')

Rtraj.DataVariables

import cartopy.crs as ccrs
import cartopy

fig,ax = plt.subplots(figsize=(10,10),subplot_kw={'projection': ccrs.PlateCarree()})
ax.plot(Rtraj.LONGITUDE,Rtraj.LATITUDE,'o')

ax.coastlines()
ax.add_feature(cartopy.feature.OCEAN)
ax.gridlines(draw_labels=True, x_inline=False, y_inline=False)

fig,ax = plt.subplots(figsize=(8,8))
ax.plot(Rtraj.PSAL,Rtraj.TEMP,'o')

Rtraj.PRES

