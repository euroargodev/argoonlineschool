# Argo Online School

In this repository you can find the python jupyter notebooks that are part of the Argo Online school. These notebooks are based on <img src="https://raw.githubusercontent.com/euroargodev/argopy/master/docs/_static/argopy_logo_long.png" alt="argopy logo" width="100"/>, [the Argo data python library](https://github.com/euroargodev/argopy), and cover the following lessons:

## Usage
First, I suggest to create a python enviroment to use these notebooks. To create, and activate, the enviroment AOS [stand for Argo Online School]:
```
conda env create -f environment.yml
conda activate AOS
```
This enviroment already includes argopy stable version.

Then, you can download the following jupyter notebooks, one for each lesson.


## Lessons included

- ### Basics of netCDF.

netCDF format description.
Using netcdf data.

- ### Argo Data system
geo
dac
- ### Real time data

- ### Delayed mode data.

- ### Quality control flags.

- ### How to take advantage of Argo data.

- ### Scientific examples. Product generation.


## Data
Data in here is used as examples, you can dowload it from:
have pre-downloaded all teh data in ./Data/, however you can use this code for dowloading it:

## For lesson 01
Daily NOAA OI SST V2 High Resolution Dataset for 2009:
`! wget ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc`

## For lesson 02
First profile of float 6900772
`! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6900772/profiles/D6900772_001.nc`
Data in the north Atlantic for the 11th November 2019
`! wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`


## References

As a very useful first aproach to python, here, you can find [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro) and [Research computing in earth Sciences](https://rabernat.github.io/research_computing/) developed by [Ryan Abernathey](https://ocean-transport.github.io/) and Kerry Key.

[Argo Stereing Team web page](http://www.argo.ucsd.edu/)
