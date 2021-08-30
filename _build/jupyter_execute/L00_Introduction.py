#!/usr/bin/env python
# coding: utf-8

# <img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoAoS.png" alt="argopy logo" width="100"/>
# 
# # Argo Online School
# 
# The Argo Online school is a set of videos and hands-on jupyter notebooks to describe the minimum requiremets to use and understand, the Argo data. 
# 
# You can access the hands-on content here in a [JubyterBook](https://euroargodev.github.io/argoonlineschool) or download it and use in your local machine. In that case, you should create a python enviroment to use these notebooks. To create and activate the AOS enviroment
# 
# ```
# conda env create -f environment.yml
# conda activate AOS
# ```
# 
# if any library is missed you should install them using, for instance:
# 
# ```
# pip install netcdf4
# pip install xarray
# pip install seawater
# ```
# 
# This enviroment already includes the last stable version of [argopy](https://argopy.readthedocs.io/en/latest/), the python library for Argo data.
# 
# ## Data
# If you download the notebooks you should create a ./Data* folder to include the files used for the examples. The files in the Data folder can be dowloaded from [here](https://www.oceanografia.es/argoonlineschool/Data/) or directly from its source using _wget_, for instance:
# 
# for the *Daily NOAA OI SST V2 High Resolution Dataset for 2009*:
# 
# `! wget ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc`
# 
# for the data from float 6900772:
# 
# `wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6900772/*`
# 
# or for the data in the north Atlantic for the 11th November 2019
# 
# `! wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`
# 
# ## Further reading
# 
# As a very useful first aproach to python, you can use [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro) and [Research computing in earth Sciences](https://rabernat.github.io/research_computing/) developed by [Ryan Abernathey](https://ocean-transport.github.io/) and Kerry Key.
# 
# For the full description of the formats and files produced by the Argo Data Assembly Centres (DACs), see the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/), the [Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/) or the [The Argo data management handbook](http://www.argodatamgt.org/content/download/340/2645/file/argo_data_management_handbook.pdf)
# 
# More information can be found in the [Argo Steering Team web page](http://www.argo.ucsd.edu/) or the [Argo Data Management team documentation](http://www.argodatamgt.org/Documentation)
# 

# **Before proceding, let's check if you really need this course** 
# Try to answer the following questions**
# 
# - what is a WMO number ?
# - what is the difference between Delayed and Real Time data mode ?
# - what is an adjusted parameter ?
# - what a QC flag of 3 means ?
# 
# If you don’t answer to more than 1 questions, please keep reading (or watching). Even though if you answered all the questions but you are not very familiar with python, netCDF, or argopy, you may find interesting the content of this course.

# In[ ]:




