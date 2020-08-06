# Accesing argo data by float

## Real Time and Calibrated data 

Since the target is to have the Argo data available within 24 hours of their transmission from the float, this data is called *Real Time* (RT) data.  One year after the data were observed it is, if necessary, adjusted and made public, this data is called *Delayed Mode* (DM). We will begin by focusing in the real time data, and in section [Adjusted data](https://euroargodev.github.io/argoonlineschool/L50_AdjustedData.html) we will describe how the data is adjusted.

## Data files organized by float

<img src="https://github.com/euroargodev/argoonlineschool/raw/master/images/dac.png" alt="xarray logo" width="650"/>

When accessing the **da**c folder in any of the *FTP* or *HTTP* sites of any of the two GDACs you will find several (11) folders, one for each of the DACs.  Within each one of these folder there is one folder for each one of the floats processed by this particular *DAC*. 

In the example here, we will use data from float with **WMO** number 6901254, that is proceesed by coriolis (later we will see how to find the DAC for each float), therefore within the folder `./6901254`, we find the following files and folder:

- 6901254_Rtraj.nc 
- 6901254_meta.nc  
- 6901254_prof.nc  
- 6901254_tech.nc  
- ./profiles

we will describe the content of each of these files later, but let's focus on the folder `./profiles/` since it contains one file for each one of the hydrographic cycles carried out by the float. **R6901254_001.nc** is the file that contains the data from the first cycle. It begins with a *R* since it is the real time data, if it began with an *D* it would be adjusted data, or Delayed Mode data; we will see and example in section [**ACTUALIZAR**]. 

Additionally some argo floats, as 6901254, also made obserations in the first descent from the surface to the parking depth, in this case the name of the files with this data would be **R6901254_001D.nc**.  

In general, the format of the file names for individual profiles are `<R/D><FloatWmoID>_<XXX><D>.nc` where :

- The initial *R* indicates Real-Time data, the initial *D* indicates Delayed-Mode data
- *XXX* is the cycle number
- The second *D* indicates a descending profile, if exist, while profiles without this D are collected during ascent.


Note that it may happens that, in the future, you try to downdload the fles from float 6901254 and there is not `R6901254_001.nc` and `R6901254_001D.nc` files, but you find `D6901254_001.nc` and `D6901254_001D.nc` since the R-files are substituded by the D-files once the data is adjusted, we will describe that in detail in section [**ACTUALIZAR**]

>The data from the float is pre-downloaded in the *./Data* folder, but you can dowload it from the Coriolis GDAC. See the [Data](https://euroargodev.github.io/argoonlineschool/README.html#data) section for instructions on how to download the data.



## Reading an Argo CTD cycle data - the building block of Argo

### The first cycle

<img src="https://github.com/euroargodev/argoonlineschool/raw/master/images/ArgoCycle.png" alt="ArgoCycle" width="1200"/>

An **Argo cycle** starts with a descent toward deep water, usually from the surface, and ends after the next programmed ascent to the surface (see the figure). During the surface interval, data transmission typically occurs but it is not a requirement for a cycle to have occurred, but if ocurrs, the cycle ends after the full surface interval has been completed.

Measurements (e.g. pressure, temperature, salinity) are performed during ascent, occasionally during descent, and  subsurface measurements during parking are sometime performed.

Each cycle of a float has a unique number, increased by one after each ascent to the surfce or shallow water. Float cycle numbers usually start at 1. The next cycles are increasing numbers (e.g. 2, 3,...N). Some floats report a cycle 0, called *launch cycle*, that is shorther than the regular cycles. The cycle time is therefore regular only for later profiles and may be variable if the float is reprogrammed after its deployment.

For those floats with cycle 0, if there is an initial descend profile, it would be on cycle 0.

First, import libraries

import numpy as np
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
%matplotlib inline

cy1  = xr.open_dataset('./Data/6901254/profiles/R6901254_001.nc')

Printing the object gives you summary information

cy1

We see how useful is the **Self-Describing** propierty of the netCDF format. Let's focus in the core variables, TEMP, SALT and PRES. Although we could inspect the previous print-out of the *cy1* dataset, we can use the data itself:

print(f"The core variables are: \n TEMP {cy1.TEMP.long_name} \n PSAL {cy1.PSAL.long_name} and \n PRES{cy1.PRES.long_name}")

print(f"The dimesions of TEMP are:\n {cy1.TEMP.dims[0]}:{cy1.TEMP.shape[0]} \n {cy1.TEMP.dims[1]}:{cy1.TEMP.shape[1]}")

We note that for for the first cycle there are two profiles (N_PROF=2) and 95 vertical levels... lets plot them:

fig, ax = plt.subplots(1,2,figsize=(8,10))

#Temperature
ax[0].plot(cy1.TEMP[0],-cy1.PRES[0],'b-',label='N_PROF=0')
ax[0].plot(cy1.TEMP[1],-cy1.PRES[1],'r.',label='N_PROF=1')
ax[0].set_title(cy1.TEMP.long_name)
ax[0].set_ylabel(cy1.PRES.long_name)
ax[0].grid()
ax[0].legend()

#Salinity
ax[1].plot(cy1.PSAL[0],-cy1.PRES[0],'b-',label='N_PROF=0')
ax[1].plot(cy1.PSAL[1],-cy1.PRES[1],'ro',label='N_PROF=1')
ax[1].set_title(cy1.PSAL.long_name)
ax[1].grid()

This is, within the cycle file, there area two profiles. The first one (N_PROF=0 in blue) it is measured during its ascend from 2000 dbar to 5 dbar and it constitutes the core argo program; the second one (N_PROF=1 in red) only measures the top 5 dbar. 

Once again all the information is in the netcf file, the data variable *VERTICAL_SAMPLING_SCHEME* contains all the details:

print(f"The first profile is the: { str(cy1.VERTICAL_SAMPLING_SCHEME[0].astype(str).values) }")

print(f"The second profile is the: {cy1.VERTICAL_SAMPLING_SCHEME[1].astype(str).values}")

Ago floats may measure several profiles in each cycle, however as a rule of thumb the first profile is always the **core mission argo CTD profile** (2000 dbar - 5 dbar). In the case of this float there is an additional second profile, with higher resolution (10 sec sampling and 1 dbar average) but unpumped, this is the sensor of conductity (for salinity) is not pumping water through to avoid contamination or biodeposition from the surface. The data from this second profile is used, mostly, for calibrations of SST observations from satellite.

In the *Reference table 16: vertical sampling schemes* of the *Argo Data Management Team. Argo user’s manual. https://doi.org/10.13155/29825* there is a description of all the different options in VERTICAL_SAMPLING_SCHEME. However a discusion of all of them is beyond the objective of this AoS than focus on understanding the basic concepts.

### The descending profile
As mentioned before, some floats also make measurmentes in the first descending phase of the first cycle, the data is in the <R/D><FloatWmoID>_001D.nc file

cy1D = xr.open_dataset('./Data/6901254/profiles/R6901254_001D.nc')

print(f"The dimesions of TEMP are:\n {cy1D.TEMP.dims[0]}:{cy1D.TEMP.shape[0]} \n {cy1D.TEMP.dims[1]}:{cy1D.TEMP.shape[1]}")

in this case there is only one profile, let's plot it together with the ascending data (cy1):


fig, ax = plt.subplots(1,2,figsize=(8,10))

#Temperature
ax[0].plot(cy1D.TEMP[0],-cy1D.PRES[0],'k-',label='N_PROF=0 Descending',linewidth=3.0)
ax[0].plot(cy1.TEMP[0],-cy1.PRES[0],'b-',label='N_PROF=0 Ascending')
ax[0].plot(cy1.TEMP[1],-cy1.PRES[1],'ro',label='N_PROF=1 Ascending')
ax[0].set_title(cy1.TEMP.long_name)
ax[0].set_ylabel(cy1.PRES.long_name)
ax[0].grid()
ax[0].legend()

#Salinity
ax[1].plot(cy1D.PSAL[0],-cy1D.PRES[0],'k-',label='N_PROF=0 Descending',linewidth=3.0)
ax[1].plot(cy1.PSAL[0],-cy1.PRES[0],'b-',label='N_PROF=0 Ascending')
ax[1].plot(cy1.PSAL[1],-cy1.PRES[1],'ro',label='N_PROF=1 Ascending')
ax[1].set_title(cy1.PSAL.long_name)
ax[1].grid()

As indicated in the figura, the first descending is only until the parking depth.

### Geographical information
The netcdf file include the information about the geographical postion of the observations (LONGITUDE and LATITUDE) and the date of the observation (JULD)

for variable in ['LONGITUDE', 'LATITUDE' , 'JULD']:
   print(f"The {cy1.data_vars[variable].long_name} is in the variable {variable}")

Let's plot it

fig, ax = plt.subplots(figsize=(8,8))

ax.plot(cy1D.LONGITUDE[0],cy1D.LATITUDE[0],'ko',label='001D N_PROF=0 Descending')
ax.plot(cy1.LONGITUDE[0],cy1.LATITUDE[0],'bo',label='001 N_PROF=0 Ascending')
#ax.set_title(cy1..long_name)
ax.set_xlabel(cy1.LONGITUDE.long_name)
ax.set_ylabel(cy1.LATITUDE.long_name)
ax.text(cy1D.LONGITUDE[0],cy1D.LATITUDE[0],'Date of observation for 001D:'+cy1D.JULD[0].values.astype(str), fontsize=14)
ax.text(cy1.LONGITUDE[0],cy1.LATITUDE[0],'Date of observation for 001:'+cy1.JULD[0].values.astype(str), fontsize=14)
ax.grid()
ax.legend();

The 2 ascending profiles in 001 have, obviously, the same time stamp:

print(cy1.JULD[0].values.astype(str))
print(cy1.JULD[1].values.astype(str))

Note that for some floats there is a <R/D><FloatWmoID>_000.n or even a <R/D><FloatWmoID>_000D.n file.

### Meta information in the cycle file
The netcdf file for each cycle includes a lot of additional information about each one of the profiles in it. Let's take a look of the basic information. 

print(f"For cycle {cy1D.CYCLE_NUMBER.astype(int).values} The {cy1D.DIRECTION.long_name} (DIRECTION) is {cy1D.DIRECTION.values.astype(str)}")
print(f"For cycle  {cy1.CYCLE_NUMBER.astype(int).values} the {cy1.DIRECTION.long_name}  (DIRECTION) is {cy1.DIRECTION.values.astype(str)}")

A is for ascending and D for descending.

And all the meta information of the float, and for each profile within each cycle, among others:

for variable in ['PLATFORM_NUMBER','DATA_CENTRE','PROJECT_NAME','PI_NAME']:
   print(f"The {cy1.data_vars[variable].long_name} ({variable}) is {cy1.data_vars[variable].values.astype(str)}")

We can also access the dimession that define the profile

for key in cy1.dims.keys():
    print(key,cy1.dims[key])

N_LEVELS is the number of vertical leves, i.e. in pressure. N_PROF the number of profiles within the cycle, as we saw previously and N_PARAM is te number of paramters, 3 for this float: TEMP, PSAL and PRES

Later we will explain N_CALIB and N_HISTORY

## Meta data
There is a lof of additional meta information in the `<FloatWmoID>_meta.nc` file

Mdata = xr.open_dataset('./Data/6901254/6901254_meta.nc')

Always we have the basic information than appers in all the netcdf files of an Argo float:

for variable in ['PLATFORM_NUMBER','DATA_CENTRE','PROJECT_NAME','PI_NAME']:
   print(f"The {Mdata.data_vars[variable].long_name} ({variable}) is {Mdata.data_vars[variable].values.astype(str)}")

and some examples of addtional information

for variable in ['FIRMWARE_VERSION','BATTERY_TYPE','DEPLOYMENT_PLATFORM','CONFIG_PARAMETER_NAME','SENSOR_SERIAL_NO']:
   print(f"The {Mdata.data_vars[variable].long_name} ({variable}) is {Mdata.data_vars[variable].values.astype(str)}")

The full descritpion of variables is in the **Argo user's Manual**




```{toctree}
:hidden:
:titlesonly:


L21_ArgoDatabyFloat_Prof
L22_ArgoDatabyFloat_Traj
L23_ArgoDatabyFloat_ArgoPy
```
