#!/usr/bin/env python
# coding: utf-8

# # Real Time quality control data

# Real-Time quality control is a set of automatic procedures that are performed in the National Data Acquisition Centers (DACs) to carry out the first quality control of the data. 
# There are a total of 19 tests that aim, to say, easy to identify anomalies in the data, because the subtle anomalies, that need a lot of expertise, and time, to discern between sensor malfunctioning and natural variability are left for the deleted mode quality control. 
# 
# The results of the real-time tests are summarized in what is called the **quality control flags**. Quality control flags are an essential part of Argo.

# ## Quality Control flags
# 
# Each observation after the RT quality control has a QC flag associated, a number from 0 to 9, with the following meaning:

# |QCflag|Meaning|Real time description|
# |:----:|:-----:|:-------------------:|
# |0 |No QC performed|No QC performed|
# |1 |Good data|All real time QC tests passed|
# |2 |Probably good data|	Probably good|
# |3 |Bad data that are potentially correctable|Test 15 or Test 16 or Test 17 failed and all other real-time QC tests passed. These  data are not to be used without scientific correction. A flag ‘3’ may be assigned by an operator during additional visual QC for bad |data that may be corrected in delayed mode.|
# |4 |Bad data|Data have failed one or more of the real-time QC tests, excluding Test 16. A flag ‘4’ may be assigned by an operator during additional visual QC for bad data that are not correctable.|
# |5 |Value changed|Value changed|
# |6 |Not currently used |Not currently used|
# |7 |Not currently used |Not currently used|
# |8 |Estimated |Estimated value (interpolated, extrapolated or other estimation)|
# |9 |Missing value|Missing value|

# Let's see how this information is stored in the NetCDF files

# In[1]:


import numpy as np
import netCDF4
import xarray as xr

import cartopy.crs as ccrs
import cartopy

import matplotlib as mpl
import matplotlib.cm as cm
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Before accesing the data, let's create some usefull colormaps and colorbar makers to help us to understand the QC flags

# In[2]:


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


# open the daily data set from the 11th november 2019

# In[3]:


dayADS = xr.open_dataset('./Data/atlantic_ocean/2019/11/20191111_prof.nc')


# In[4]:


dayADS


# Beside the core variables, TEMP, PSAL and PRES, we also have the variables TEMP_ADJUSTED, PSAL_ADJUSTED and PRES_ADJUSTED, that correspond to DM, or calibrated data. However, here we keep the focus in the Real Time data, and in the next section we will use the calibrated data.
# 
# Let's begin by plotting all the data. We will use a [TS diagram](http://www.physocean.icm.csic.es/ShelfCoast/chapter10-en.html)

# In[4]:


fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(dayADS.PSAL, dayADS.TEMP, cmap=qcmap)
ax.grid()


# In[5]:


pres=dayADS.PRES
lon=dayADS.LONGITUDE+pres*0
lon


# In[6]:


cycle=dayADS.CYCLE_NUMBER+pres*0


# In[7]:


fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(lon, pres, c=dayADS.PSAL_QC, vmin=0, vmax=9, cmap=qcmap)
colorbar_qc(qcmap, ax=ax)
ax.grid()
ax.set_ylim(0,2000)
ax.invert_yaxis()
ax.set_xlabel(f"{dayADS.PSAL.long_name}")
ax.set_ylabel('Pressure')
ax.set_title('PSAL_QC');


# In[8]:


l=dayADS.PSAL_QC[0,0]
print(dayADS.PSAL.where(dayADS.PSAL_QC.values.astype(float) == 1))


# In[9]:


fig, ax = plt.subplots(figsize=(20,10))
sc = ax.scatter(dayADS.PSAL.where(dayADS.PSAL_QC.values.astype(float) == 1), 
                dayADS.TEMP.where(dayADS.PSAL_QC.values.astype(float) == 1))
ax.grid()


# In[ ]:




