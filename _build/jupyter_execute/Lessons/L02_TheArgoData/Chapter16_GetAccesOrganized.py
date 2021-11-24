#!/usr/bin/env python
# coding: utf-8

# # Where can I get access to data and how is it organized?

# **[HOST - Video 206-01] Where can I get access to data and how is it organized? - Host - INT. (White background)**

# **[ANIMATION 206-02] Servers (represent servers and data centers in the background)**

# **[ANIMATION Video 206-03] FTP and HTTP Servers**

# **[TUTORIAL 206-04] FTP access**

# Each data will have a specific quality flag assigned that indicates its status! Both Real-Time quality control and Delayed - Mode quality control follow a solid quality flag policy. Here are some examples that show how robust this quality flag policy is:
# 
# • The value assigned by a test cannot override a higher value from a previous test. Taking the Real-Time quality control as an example: a QC flag ‘4’ (bad data) set by Test 11 (gradient test) cannot be decreased to QC flag ‘3’ (bad data that is potentially correctable) set by Test 15 (gray list).
# 
# • A measurement with QC flag '4' (bad data) or '3' (bad data that are potentially correctable) cannot get a better QC flag in other quality control tests.
# 
# • Since salinity (PSAL) is almost always calculated from temperature (TEMP) and conductivity (CNDC), if the temperature is flagged '4' (or '3'), then salinity is also flagged as '4' (or '3').
# 

# **[GRAPHIC 205-04] Flags
# https://argo.ucsd.edu/data/how-to-use-argo-files/**
