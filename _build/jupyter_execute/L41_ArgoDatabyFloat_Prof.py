# Accessing all profiles at once 

Convenetly, all the core mision profiles are compated in a single file `<FloatWmoID>_prof.nc` 

import numpy as np
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
%matplotlib inline

prof  = xr.open_dataset('./Data/6901254/6901254_prof.nc')

In this case, N_PROF is 66, since there are 66 two for the first cycle, the descending and the ascending. This profiles are just the 'Primary sampling', if you need the high resotuion upper 5dbar you ave to use the indvidual cycle files.

fig , ax = plt.subplots(figsize=(10,10))
ax.contourf(prof.PSAL,40)

However, if we want to add the proper pressure levels, since each profile have slighly different levels

prof.PRES[3,:].values

prof.PRES[4,:].values

we will need to do a little of interpolation to use contour:

juld=prof.JULD.values
psal=prof.PSAL.values
pres=prof.PRES.values
prei=np.arange(5,2005,5)

psali= np.zeros((juld.shape[0],prei.shape[0]))
psali.fill(np.nan)

for ip in range(0,66):
    psali[ip,:]=np.interp(prei,pres[ip,:],psal[ip,:])

fig, ax = plt.subplots(figsize=(15,10))

cs=ax.contourf(juld,prei,psali.transpose(),40,cmap="RdBu_r")
cs2=ax.contour(juld,prei,psali.transpose(),colors=('k'), levels=cs.levels[::4])

ax.invert_yaxis()
ax.clabel(cs2, fmt='%2.1f', colors='w', fontsize=10)

ax.set_title(f"Vertical Salinity section for float {prof.PLATFORM_NUMBER[0].astype(str).values}")
ax.set_xlabel(f"{prof.JULD.standard_name}")
ax.set_ylabel(f"{prof.PRES.long_name}")

cbar=fig.colorbar(cs,ax=ax)

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(prof.PSAL,prof.TEMP,c=prof.PRES)

### metadata

