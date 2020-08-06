<img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoAoS.png" alt="argopy logo" width="100"/>

# Argo Online School

The Argo Online school is a set of videos and hands-on jupyter notebooks to describe the minimum requiremets to use, and understand, the Argo data. You can access the content as here in a [JubyterBook](https://euroargodev.github.io/argoonlineschool), or download them and use in your local machine. In that case, you should create a python enviroment to use these notebooks. To create, and activate, the enviroment AOS 

```
conda env create -f environment.yml
conda activate AOS
```

This enviroment already includes argopy stable version.

## Data
If you download the notebooks you should create a ./Data* folder where include the files used for the examples. To download the files you should 

Daily NOAA OI SST V2 High Resolution Dataset for 2009:

`! wget ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc`

Data from float 6900772

`wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/*`

Data in the north Atlantic for the 11th November 2019

`! wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`

## Further reading

As a very useful first aproach to python, you can use [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro) and [Research computing in earth Sciences](https://rabernat.github.io/research_computing/) developed by [Ryan Abernathey](https://ocean-transport.github.io/) and Kerry Key.

For the full description of the formats and files produced by the Argo Data Assembly Centres (DACs), see the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/), the [Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/) or the [The Argo data management handbook](http://www.argodatamgt.org/content/download/340/2645/file/argo_data_management_handbook.pdf)

More information can be found in the [Argo Stereing Team web page](http://www.argo.ucsd.edu/) or the [Argo Data Management team documentation](http://www.argodatamgt.org/Documentation)





```{toctree}
:hidden:
:titlesonly:


L10_TheArgoProgram
L20_ArgoDatabyFloat
L30_ArgoDatabyDate
L40_RTQualityControl
L50_AdjustedData
```
