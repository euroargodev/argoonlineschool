# Accessing all profiles at once 

Convenetly, all the core mision profiles are compated in a single file `<FloatWmoID>_prof.nc` 

**6901254/6901254_prof.nc**

import numpy as np
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
%matplotlib inline

prof  = xr.open_dataset('./Data/6901254/6901254_prof.nc')

In this case, N_PROF is 66, since there are 66 two for the first cycle, the descending and the ascending. This profiles are just the 'Primary sampling', if you need the high resotuion upper 5dbar you ave to use the indvidual cycle files.

fig , ax = plt.subplots(figsize=(10,10))
ax.contourf(prof.PSAL,40);

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

for ip in range(0,pres.shape[0]-1):
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

or a TS diagram using the hydrographic data in `TEMP` and `PSAl`

import seawater as sw

temp=prof.TEMP.values.flatten()
psal=prof.PSAL.values.flatten()
pres=prof.PRES.values.flatten()

ptmp=sw.ptmp(psal, temp, pres, pr=0)

t_bins = np.linspace(2, 25, 200)
s_bins = np.linspace(35, 37.25, 200)

hist, xedges, yedges = np.histogram2d(psal, ptmp, (s_bins, t_bins))
xidx = np.clip(np.digitize(psal, xedges), 0, hist.shape[0]-1)
yidx = np.clip(np.digitize(ptmp, yedges), 0, hist.shape[1]-1)
c = hist[xidx, yidx]

fig, ax = plt.subplots(figsize=(10,10))
sc=ax.scatter(psal, ptmp, c=c,alpha=0.5, cmap="RdBu_r",vmin=0, vmax=10)
ax.set_title(f"T/S diagram for float {prof.PLATFORM_NUMBER[0].astype(str).values}")
ax.set_ylabel("potential temperature")
ax.set_xlabel(f"{prof.PSAL.long_name}")
fig.colorbar(sc,extend='both');

### Metadata

all the metadata information for each profile is included:

for i1 in range(1,prof.dims['N_PROF'],10):
    print(f"Cycle {prof.data_vars['CYCLE_NUMBER'].values.astype(int)[i1]}"
          f" Direction {prof.data_vars['DIRECTION'].values.astype(str)[i1]}"
          f" WMO {prof.data_vars['PLATFORM_NUMBER'].values.astype(str)[i1]}"
          f" Data Center {prof.data_vars['DATA_CENTRE'].values.astype(str)[i1]}"   
          f" Project {prof.data_vars['PROJECT_NAME'].values.astype(str)[i1]}" )