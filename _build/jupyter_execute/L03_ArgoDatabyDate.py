# <img src="./images/logoArgo.png" alt="Argo status" width="150"/> Argo data by date



## Data files organized by date

<img src="https://github.com/PedroVelez/argoonlineschool/raw/master/images/geo.png" alt="geo organization" width="650"/>


The geographical limits of Atlantic, Pacific and Indian oceans are:

- The Pacific/Atlantic frontier is 70°W.
- The Pacific/Indian frontier is 145°E.
- The Atlantic/Indian frontier is 20°E. 

In each directory the data is organized by **year**, **month** and **day**, according to the date of the beginning of the profile.

Lets use data in the *Atlantic for the 11th November 2019*. It is pre-downloaded in the ./Data folder, but you can dowload it from the Coriolis GDAC:

`! wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`

import netCDF4
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

xrDS = xr.open_dataset('./Data/20191111_prof.nc')
xrDS

fig, ax = plt.subplots(figsize=(14,8))
ax.plot(xrDS.LONGITUDE,xrDS.LATITUDE,'o')
ax.grid()

