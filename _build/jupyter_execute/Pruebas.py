import netCDF4
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

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