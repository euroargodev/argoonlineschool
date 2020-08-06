import netCDF4
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

from argopy import DataFetcher as ArgoDataFetcher
plt.style.use('default')
argo_loader = ArgoDataFetcher()
argo_loader = ArgoDataFetcher(backend='erddap')
argo_loader = ArgoDataFetcher(cachedir='tmp')

apDS2 = argo_loader.profile(6900944,10).to_xarray()
data  = apDS2.argo.point2profile()
data

cy0D  = xr.open_dataset('/Volumes/OkapiBU/Data/Argo/dac/coriolis/6900944/profiles/D6900944_000D.nc')
cy0  = xr.open_dataset('/Volumes/OkapiBU/Data/Argo/dac/coriolis/6900944/profiles/D6900944_000.nc')
cy1  = xr.open_dataset('/Volumes/OkapiBU/Data/Argo/dac/coriolis/6900944/profiles/D6900944_001.nc')
cy2  = xr.open_dataset('/Volumes/OkapiBU/Data/Argo/dac/coriolis/6900944/profiles/D6900944_002.nc')

print(cy0.DATA_MODE.values.astype(str)[0])

fig, ax = plt.subplots(1,3,figsize=(8,10))
print(f"{str(cy0D.JULD)}")
print(f"{str(cy0.JULD)}")
print(f"{str(cy1.JULD)}")
print(f"{str(cy2.JULD)}")
#Temperature
ax[0].plot(cy0D.TEMP[0],-cy0D.PRES[0],'bo',label='N_PROF=0')


ax[1].plot(cy0.TEMP[0],-cy0.PRES[0],'yo',label='N_PROF=0')
ax[2].plot(cy1.TEMP[0],-cy1.PRES[0],'ro',label='N_PROF=0')

## Remote data access via openDAP

With OPeNDAP, you can access data using an URL rather than a local path. For xarray it is like having the file locally, the only difference is that you provide a differente path.

OPeNDAP stand for *Open-source Project for a Network Data Access Protocol* [More information here](https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api/opendap)

https://www.psl.noaa.gov/data/gridded_help/using_dods.html

base_url = '/Volumes/OkapiBU/BackUP/Dropbox/Oceanografia/Data/Satelite/noaa.oisst.v2.highres/Data/sst.day.mean'
files = [f'{base_url}.{year}.nc' for year in range(1982, 2019)]


ds = xr.open_mfdataset(files)
ds

sst = ds.sst
sst.sel(lon=(360-18), lat=28, method='nearest').plot()