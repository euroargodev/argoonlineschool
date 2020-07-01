# Argo data by float

## Data files organized by float

<img src="https://github.com/PedroVelez/argoonlineschool/raw/master/images/dac.png" alt="xarray logo" width="650"/>

Accessing the *dac* folder in any of the FTP or HTTP sites of andy of the GDAC you will find several folders, one for each of the DACs. As indicated in the figure, within each folder there is a folder for each one of the floats that is processed by this DAC.

The number is knwon as the **World Meteorological Organization (WMO)** identifier and it is unique for each float.

Lets use data from the first profile of float 6901254. It is pre-downloaded in the *./Data* folder, but you can dowload it from the Coriolis GDAC:
```
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/6901254_meta.nc
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/6901254_prof.nc
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/6901254_tech.nc
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/6901254_Rtraj.nc
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/profiles/R6901254_001.nc 
! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/profiles/R6901254_001D.nc
```

Note that it may happens that, in the future, you try to downdload the fles and there is not `R6901254_001.nc` and `R6901254_001D.nc` files, and you may find `D6901254_001.nc` and `D6901254_001D.nc` the fist *D* is for Delayed Mode. We will see its meaning in the following chapter, hence if you can not download them, use the copy in `./Data`

import netCDF4
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

xrDS1 = xr.open_dataset('./Data/6901254/profiles/R6901254_001.nc')
xrDS1



fig, ax = plt.subplots(figsize=(8,8))
ax.plot(xrDS1.PSAL,xrDS1.TEMP,'bo')
ax.grid()
print(xrDS1.JULD[0])

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

