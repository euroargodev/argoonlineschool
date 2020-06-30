# Argo data by float

## Data files organized by float

<img src="https://github.com/PedroVelez/argoonlineschool/raw/master/images/dac.png" alt="xarray logo" width="650"/>

Accessing the *dac* folder in any of the FTP or HTTP sites of andy of the GDAC you will find 11 folders, one for each of the DACs. As indicated in the figure, within each folder tehre is a folder for each one of the floatos. The number is knwon as the World Meteorological Organization (WMO) ID and it isunique for each float.

Lets use data from the first profile of float 6900772. It is pre-downloaded in the *./Data* folder, but you can dowload it from the Coriolis GDAC:

`! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6900772/profles/D6900772_001.nc`

import netCDF4
import xarray as xr
from matplotlib import pyplot as plt
%matplotlib inline

xrDS = xr.open_dataset('./Data/D6900772_001.nc')
xrDS

fig, ax = plt.subplots(figsize=(8,8))
ax.plot(xrDS.PSAL,xrDS.TEMP,'o')
ax.grid()

