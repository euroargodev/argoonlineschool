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

qcmap = mpl.colors.ListedColormap(['#000000' , '#31FC03' , '#ADFC03' , '#FCBA03' ,'#FC1C03',
                                   '#324CA8' , '#000000' , '#000000' , '#B22CC9', '#000000'])
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

for iwmo in [1900379,
             4900556,4900557,4900558,6900230,6900231,6900506,
             6900635,6900636,6900659,6900660,6900661,6900662,6900760,
             6900761,6900762,6900763,6900764,6900765,6900766,6900767,
             6900768,6900769,6900770,6900771,6900772,6900773,6900774,
             6900775,6900776,6900777,6900778,6900779,6900780,6900781,
             6900782,6900783,6900784,6900785,6900786,6900787,6900788,
             6900789,6901237,6901238,6901239,6901240,6901241,6901242,
             6901243,6901244,6901245,6901246,6901247,6901248,6901249,
             6901250,6901251,6901252,6901253,6901254,6901255,6901256,
             6901257,6901258,6901259,6901260,6901262,6901263,6901264,
             6901265,6901266,6901267,6901268,6901269,6901270,6901271,
             6901272,6901273,6901274,6901275,6901276,6901277,6901278,
             6901279,6901280,6901281
]:
    file=f"/Users/pvb/Dropbox/Oceanografia/Data/Argo/Floats/{iwmo}/{iwmo}_prof.nc"
    dayADS = xr.open_dataset(file)
    
    pres=dayADS.PRES
    cycle=dayADS.CYCLE_NUMBER+pres*0
    fig, ax = plt.subplots(2,1,figsize=(10,10))
    sc = ax[0].scatter(cycle, pres, c=dayADS.PSAL_QC, vmin=0, vmax=9, cmap=qcmap)
    colorbar_qc(qcmap, ax=ax)
    ax[0].set_title(f"{iwmo}")
    ax[0].grid()
    ax[0].set_ylim(0,2000)
    ax[0].invert_yaxis()
   
    
    sc1 = ax[1].plot(dayADS.PSAL, dayADS.TEMP, 'or')
    sc2 = ax[1].plot(dayADS.PSAL_ADJUSTED, dayADS.TEMP_ADJUSTED, 'ob')
    ax[1].set_title(f"{iwmo}")
    ax[1].grid()
    fig.savefig(f"{iwmo}.pdf")

