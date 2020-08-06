# Quality Control of the Argo data

So far we have used the real time data, but without attending to any quality control.
The Argo network provides both quality control (QC) flags and errors to help users decide if they want to use the data or not. There are flags for both the raw and adjusted data. Let's focus on the Real Time data.

## Quality Control flags
The flags are:

|QCflag|Meaning|Real time description|
|:----:|:-----:|:-------------------:|
|0 |No QC performed|No QC performed|
|1 |Good data|All real time QC tests passed|
|2 |Probably good data|	Probably good|
|3 |Bad data that are potentially correctable|Test 15 or Test 16 or Test 17 failed and all other real-time QC tests passed. These  data are not to be used without scientific correction. A flag ‘3’ may be assigned by an operator during additional visual QC for bad |data that may be corrected in delayed mode.|
|4 |Bad data|Data have failed one or more of the real-time QC tests, excluding Test 16. A flag ‘4’ may be assigned by an operator during additional visual QC for bad data that are not correctable.|
|5 |Value changed|Value changed|
|6 |Not currently used |Not currently used|
|7 |Not currently used |Not currently used|
|8 |Estimated |Estimated value (interpolated, extrapolated or other estimation)|
|9 |Missing value|Missing value|

Load libraries

import numpy as np
import netCDF4
import xarray as xr

import cartopy.crs as ccrs
import cartopy

import matplotlib as mpl
import matplotlib.cm as cm
from matplotlib import pyplot as plt
%matplotlib inline

Create some usefull colormaps and colorbar makers:

qcmap = mpl.colors.ListedColormap(['#000000', 
                                   '#31FC03', 
                                   '#ADFC03', 
                                   '#FCBA03', 
                                   '#FC1C03',
                                   '#324CA8', 
                                   '#000000', 
                                   '#000000', 
                                   '#B22CC9', 
                                   '#000000'])
def colorbar_qc(cmap, **kwargs):
    """Adjust colorbar ticks with discrete colors for QC flags"""
    ncolors = 10
    mappable = cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    colorbar = plt.colorbar(mappable, **kwargs)
    colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
    colorbar.set_ticklabels(range(ncolors))
    return colorbar

open the daily data set from the 11th november 2019

dayADS = xr.open_dataset('./Data/atlantic_ocean/2019/11/20191111_prof.nc')

fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(dayADS.PSAL, dayADS.TEMP, cmap=qcmap)
ax.grid()

lon=dayADS.LONGITUDE+pres*0
lon

pres=dayADS.PRES
cycle=dayADS.CYCLE_NUMBER+pres*0

fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(lon, pres, c=dayADS.PSAL_QC, vmin=0, vmax=9, cmap=qcmap)
colorbar_qc(qcmap, ax=ax)
ax.grid()
ax.set_ylim(0,2000)
ax.invert_yaxis()
ax.set_xlabel(f"{dayADS.PSAL.long_name}")
ax.set_ylabel('Pressure')
ax.set_title('PSAL_QC');

l=dayADS.PSAL_QC[0,0]
print(dayADS.PSAL.where(dayADS.PSAL_QC.values.astype(float) == 1))

fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(dayADS.PSAL.where(dayADS.PSAL_QC.values.astype(float) == 1), 
                dayADS.TEMP.where(dayADS.PSAL_QC.values.astype(float) == 1))
ax.grid()

