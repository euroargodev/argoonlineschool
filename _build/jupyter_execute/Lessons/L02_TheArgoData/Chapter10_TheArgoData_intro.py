#!/usr/bin/env python
# coding: utf-8

# #  The Argo Data
# 
# <img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoArgo.png" alt="Argo status" width="100"/>

# In[4]:


get_ipython().run_cell_magic('HTML', '', '<center>\n<iframe width="560" height="315" src="https://drive.google.com/file/d/1hb4H2MhoKU38uHTBO1HZJDwMKLZ-Pnkz/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</center>')


# **The WMO: a unique identifier for each float**
# 
# Each one of the Argo floats has a unique identifier, known as the World Meteorological Organization (WMO). The WMO is assigned at the moment of the deployment of the float, but it is not hard-coded in the float.

# **The basis of the Argo Data System**
# 
# As explained in the videos of Lesson 2, when an Argo float surfaces, the data are received by one of the *Data Assembly Centers* (DAC). At the DACs, they are subjected to initial scrutiny using a set of real-time quality control tests where erroneous data are flagged or corrected, then the data are passed to one of the two Argo *Global Data Assembly Center* (GDAC), the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Monterey, California, USA). 
# 
# The GDACs are the first stage at which the freely available data can be obtained via the internet. The GDACs synchronize their data to ensure consistent data is available on both sites. The target is for these *real-time* data to be available within 12-24 hours of their transmission from the float.

# Additionally, Argo data can be accessed in several other ways:
# 
# - via the Global Telecommunication System for operational centers. 
# - via interactive Data selection tools on the GDACs.
# - via gridded fields and velocity products based on Argo NetCDF files from the GDACs.
# - via data viewers that incorporate Argo data.
# - via the [Global Argo Data Repository (GADR)](https://www.nodc.noaa.gov/argo/) for archived and offline data.
# - via monthly copies of the GDACs https://www.seanoe.org/data/00311/42182/
# 
# See the [Argo data sources](https://argo.ucsd.edu/data/) to read a full description, with links, to these other ways of accessing the data.
# 
# **Here we focus on the access to the primary source of the Argo data, the GDACs**

# **Data organization at the GDACS**
# 
# In the GDACS, the Argo data is organized in two different ways:
# 
# * By date, with one folder for each ocean basin, and then a folder for each year and month and a file for each day. 
# 
# * By DAC (data acquisition center) and Argo float (WMO number).
# 
# * By processing date: The last processed data organized by processing day, with access to the last 12 months.
# 
# At the early stage of the Argo program, and due to the huge amount of data that was foreseen  Argo would create, it was decided that netCDF would be the official file format for the Argo data. Hence, before explaining how to [acces Argo data by float](https://euroargodev.github.io/argoonlineschool/L20_ArgoDatabyFloat_Intro.html) or [by date](https://euroargodev.github.io/argoonlineschool/L30_ArgoDatabyDate_Intro.html) it is necessary to make a short introduction to the properties of this data format, and how to read files in **netCDF**.
# 
# 
