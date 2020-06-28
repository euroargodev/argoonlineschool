# Argo Online School

<img src="https://raw.githubusercontent.com/PedroVelez/argoonlineschool/master/images/logo.png" alt="argopy logo" width="200"/>

In this repository you can find the python jupyter notebooks that are part of the Argo Online school. These notebooks use <img src="https://raw.githubusercontent.com/euroargodev/argopy/master/docs/_static/argopy_logo_long.png" alt="argopy logo" width="100"/>, [the Argo data python library](https://github.com/euroargodev/argopy), and cover the following lessons:

## Usage
First, I suggest to create a python enviroment to use these notebooks. This enviroment already includes argopy stable version. To create, and activate, the enviroment AOS [Argo Online School]:

```
conda env create -f environment.yml
conda activate AOS
```

Then, you can download the notebooks or alternative visit the Jupyter book created


## Data
Data in the ./Data folder is used as example. Alternatively you can download it from:

Daily NOAA OI SST V2 High Resolution Dataset for 2009:

`! wget ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc`

First profile of float 6900772

`! wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6900772/profiles/D6900772_001.nc`

Data in the north Atlantic for the 11th November 2019

`! wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`

## References

As a very useful first aproach to python, you can use [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro) and [Research computing in earth Sciences](https://rabernat.github.io/research_computing/) developed by [Ryan Abernathey](https://ocean-transport.github.io/) and Kerry Key.

For the full description of the formats and files produced by the Argo Data Assembly Centres (DACs), see the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/)
[Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/)


[The Argo data management handbook](http://www.argodatamgt.org/content/download/340/2645/file/argo_data_management_handbook.pdf)
[Argo Stereing Team web page](http://www.argo.ucsd.edu/)
[Argo Data Management team documentation](http://www.argodatamgt.org/Documentation)
