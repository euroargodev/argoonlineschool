#!/usr/bin/env python
# coding: utf-8

# # Real-Time and Delayed mode data

# The Argo program guarantees free and quality data distribution to the entire scientific & operational community and the general public. Before that, data needs to be checked out through different controls to guarantee their homogeneity and quality within the established accuracy ranges (+/- 0.005ºC temperature and +/- 0.01 for salinity). 
# 
# The first control stage is the **Real-Time (RT) quality control** and the last stage is called the **Delayed - Mode (DM) quality control**. Therefore, the data that has gone through the RT quality control is called [**RT data**](https://euroargodev.github.io/argoonlineschool/L41_RTData.html) and the data that has gone through, both, the RT and DM quality controls is called [**DM data**](https://euroargodev.github.io/argoonlineschool/L41_DMData.html); although some times we also refer to this data as **calibrated data**
# 
# For both, RT and DM data, there are quality control (QC) flags and errors that the Argo network provides to help users decide to use the data or not. There are flags 
# 
# So far we have accesed only the RT data and without paying attention to its quality. In this chapter we will describe how to use the quality control information stored in the netcdf files. 

# 
# 
