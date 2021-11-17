#!/usr/bin/env python
# coding: utf-8

# # Accessing trayectory data

# First, import libraries

# In[1]:


import numpy as np
import xarray as xr
import netCDF4
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


Rtraj = xr.open_dataset('./Data/6901254/6901254_Rtraj.nc')


# In[3]:


Rtraj


# In[4]:


import cartopy.crs as ccrs
import cartopy
import numpy as np


fig,ax = plt.subplots(figsize=(10,10),subplot_kw={'projection': ccrs.PlateCarree()})
ax.plot(Rtraj.LONGITUDE,Rtraj.LATITUDE,'ob')
ax.plot(Rtraj.LONGITUDE[~np.isnan(Rtraj.LONGITUDE)],Rtraj.LATITUDE[~np.isnan(Rtraj.LATITUDE)],'-b')
ax.plot(Rtraj.LONGITUDE[0],Rtraj.LATITUDE[0],'ok')
ax.plot(Rtraj.LONGITUDE[-1],Rtraj.LATITUDE[-1],'sk')

ax.set_title(f"Data from {Rtraj.PLATFORM_NUMBER.values.astype(str)}")
ax.coastlines()
ax.add_feature(cartopy.feature.OCEAN)
ax.gridlines(draw_labels=True, x_inline=False, y_inline=False);


# In[5]:


fig,ax = plt.subplots(figsize=(10,10))
sc=ax.scatter(Rtraj.PSAL,Rtraj.TEMP,c=Rtraj.PRES)
ax.set_title(f"Vertical Salinity section for float {Rtraj.PLATFORM_NUMBER.astype(str).values}")
ax.set_xlabel(f"{Rtraj.PSAL.long_name}")
ax.set_ylabel(f"{Rtraj.TEMP.long_name}")
fig.colorbar(sc);


# In[6]:


fig,ax = plt.subplots(figsize=(15,8))
ax.plot(Rtraj.JULD,Rtraj.PRES,'-')
sc=ax.scatter(Rtraj.JULD,Rtraj.PRES,c=Rtraj.TEMP)
ax.set_xlabel(f"{Rtraj.JULD.standard_name}")
ax.set_ylabel(f"{Rtraj.PRES.long_name}")
ax.invert_yaxis()
fig.colorbar(sc);


# In[7]:


fig,ax = plt.subplots(figsize=(15,8))
ax.plot(Rtraj.JULD,Rtraj.MEASUREMENT_CODE,'o');

