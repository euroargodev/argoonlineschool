# Accesing argo data by float

First, import libraries

import numpy as np
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
%matplotlib inline

prof  = xr.open_dataset('./Data/6901254/6901254_prof.nc')

si fuerzo que todos los niveles sean iguales, funciona. por eso me da que es lo de la interpolacion. 

juld=prof.JULD.values
psal=prof.PSAL.values
pres=prof.PRES.values
prei=np.arange(5,2005,5)

prof.PRES[3,:].values

psali= np.zeros((juld.shape[0],prei.shape[0]))
psali.fill(np.nan)
for ip in range(0,66):
    psali[ip,:]=np.interp(prei,pres[ip,:],psal[ip,:])

prof.PRES[4,:].values

fig, ax = plt.subplots(figsize=(15,10))

cs=ax.contourf(juld,prei,psali.transpose(),40,cmap="RdBu_r")
cs2=ax.contour(juld,prei,psali.transpose(),colors=('k'), levels=cs.levels[::4])

ax.invert_yaxis()
ax.clabel(cs2, fmt='%2.1f', colors='w', fontsize=10)

ax.set_title(f"Vertical Salinity section for float {prof.PLATFORM_NUMBER[0].astype(str).values}")
ax.set_xlabel(f"{prof.JULD.standard_name}")
ax.set_ylabel(f"{prof.PRES.long_name}")


cbar=fig.colorbar(cs,ax=ax)

