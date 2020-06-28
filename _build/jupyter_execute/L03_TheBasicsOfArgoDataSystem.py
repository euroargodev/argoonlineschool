# ![Argo logo](http://www.argo.ucsd.edu/argocolorsmall.gif) Argo Data System

When an Argo float surfaces, the data are received by one of the *Data Assembly Centers* (DAC). At the DACs, they are subjected to initial scrutiny using a set of real time quality control tests where erroneous data are flagged or corrected, then the data are passed to one of the two Argo *Global Data Assembly Center* (GDAC), the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Mobterey, California, USA). 

The GDACs are the first stage at which the freely available data can be obtained via the internet. The GDACs synchronize their data holdings to ensure consistent data is available on both sites. The target is for these *real-time* data to be available within 24 hours of their transmission from the float.

Additionally Argo data can be accesed by several other ways:

- via the Global Telecomunication System for operational centers. 
- via interactive Data selection tools on the GDACs
- via gridded fields and velocity products based on Argo NetCDF files from the GDACs
- via data viewers that incorporate Argo data
- via the [Global Argo Data Repository (GADR)](https://www.nodc.noaa.gov/argo/) for archived and offline data
- via monthly copies of the GDACs https://www.seanoe.org/data/00311/42182/

See the [A beginner's guide to accessing Argo data](http://www.argo.ucsd.edu/Argo_date_guide.html) to read a full description, with links, to this other ways of accesing the data

**However, in this secction we focus in the accesss to the primary source of the Argo data, the GDACs**

## Using Argo data from the GDACs
For users interested in manipulating the actual Argo NetCDF files, the GDACs should be the route to access Argo data. Both GDACs offer access to the complete Argo data collection, including float metadata, detailed trajectory data, profile data and technical data all in NetCDF  

- FTPp site of the US-Godae GDAC ftp://usgodae.org/pub/outgoing/argo/
- FTP site of the Coriolis GDAC ftp://ftp.ifremer.fr/ifremer/argo
- HTTP site of the Coriolis GDAC https://data-argo.ifremer.fr

The HTTP and FTP sites are identical and are organized into three main folders: 
- a *dac* folder which sorts the data by Data Assembly Centre (DAC)
- a *geo* folder which sorts the data by ocean basin 
- a *latest_data* folder which includes the most recent data. 
There are also several index files in the top directory containing a list of metadata on each type of Argo data file (meta, prof, tech and traj) contained in the "dac" and "geo" folders. It is possible to download these lists and search them for floats in specific regions, times, DACs, etc. There is also a grelist which contains a list of floats that likely have sensor problems. We will describe this files later.

In the Argo [User's Manual and the Argo quality control manual](http://www.argodatamgt.org/Documentation) there is a full description of the naming system of the files as well as the variable names and quality control flags within each data file. **In this lessons we do an overview of all of it.**

Accessing the *dac* folder in any of the FTP or HTTP sites of andy of the GDAC you will find 11 folders, one for each of the DACs. As indicated in the figure, within each folder tehre is a folder for each one of the floatos. The number is knwon as the World Meteorological Organization (WMO) ID and it isunique for each float.

## Core parameters
JULD, LATITUDE, LONGITUDE, PRES, TEMP, PSAL and CNDC.




```{toctree}
:hidden:
:titlesonly:


L03_ArgoDatabyDAC
L03_ArgoDatabyGEO
```
