# Using Argo Data

<center>
    <iframe width="560" height="315" src="https://drive.google.com/file/d/17s5UwuNwyQzjL7EW9DYhWkAYP8nYTYLI/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> 
    </iframe>
</center>

As indicated in the introduction, the third component of the Argo Online School is  hands-on, and it is based on Jupyter Notebooks:

## The hands-on component of the Argo Online School

You can access the hands-on content as here, in a web-page, built using [JubyterBook](https://euroargodev.github.io/argoonlineschool), or download the Jupyter Notebooks and use them in your local machine. 

The hands-on component of the Argo Online School was developed using JupyterLab, since it contains a complete environment for interactive scientific computing which runs in your web browser. Jupyter is an open-source python project, and as a very useful first approach to python and JupyterLab, you can use [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro) and [Research computing in earth Sciences](https://rabernat.github.io/research_computing/) developed by [Ryan Abernathey](https://ocean-transport.github.io/) and [Kerry Key](https://emlab.ldeo.columbia.edu/index.php/team/kerry-key/).

In case that you decide to download and run the python Jupyter Notebooks in your local machine, you should create a python environment. Since using some of the packages may give problems due to compatibility issues between conda-forge packages and packages contained in the default conda channels, we will recommend to set up `channel_priority: strict` and give priority to the `conda-forge` channel over the default channels when installing stuff. There are two ways of doing it. Either you always specify `conda install -c conda-forge` or you create a .condarc file in your home with this content:
```
channels:
  - conda-forge
  - defaults
channel_priority: strict
```
An environment should either use conda-forge or not, from creation to destruction. Do not mix and match. If you created it without using the conda-forge channel, then do not add it to the mix halfway. In practice, we always create an environment with conda-forge unless in very specific cases where we found incompatibilities.

To create and activate the AOS environment, that already includes the last stable version of [argopy](https://argopy.readthedocs.io/en/latest/), the python library for Argo data, you should:

```
conda env create -n AOS -f environment.yml 
conda activate AOS
```

If by any chance, a library is not included in the environment.yml file, you should install it using, for instance:

```
conda install netcdf4
conda install xarray
conda install seawater
```


### Data used in the Argo Online School

If you download the notebooks you should create a ./Data* folder to include the files used for the examples. The files in the Data folder can be downloaded  directly from its source using _wget_, for instance:

for the *Daily NOAA OI SST V2 High-Resolution Dataset for 2019*:

```
wget ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc
```

for the data from float 6901254:

```
wget ftp://ftp.ifremer.fr/ifremer/argo/dac/coriolis/6901254/*`
```

or for the data in the North Atlantic for the 11th November 2019

```
wget ftp://ftp.ifremer.fr/ifremer/argo//geo/indian_ocean/2019/11/20191111_prof.nc`
```

However we recomend to download the data from [here](https://drive.google.com/drive/folders/19yMW3sMAFouUb0bPpoyDeZY3-QC63pqi) to use exactly the same dataset and therefore to be able to reproduce precisely the notebooks here. Once you have downloaded the data, the ./Data folder should look like:

<img src="https://github.com/euroargodev/argoonlineschool/raw/master/images/DataFolder.png" alt="ArgoCycle" width="800"/>

### Further reading

For the full description of the formats and files produced by the Argo Data Assembly Centres (DACs), see the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/), the [Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/) or the [The Argo data management handbook](http://www.argodatamgt.org/content/download/340/2645/file/argo_data_management_handbook.pdf).

More information can be found in the [Argo Steering Team web page](http://www.argo.ucsd.edu/) or the [Argo Data Management team documentation](http://www.argodatamgt.org/Documentation).


## License for this book

All content in this book (ie, any files and content in the `content/` folder)
is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
(CC BY-SA 4.0) license.
