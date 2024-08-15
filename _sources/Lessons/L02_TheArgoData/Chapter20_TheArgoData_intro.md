#  The Argo Data

<img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoArgo.png" alt="Argo status" width="100"/>


#### A big data set

In this lesson, you will get a deep approach to Argo data: Its basic features, where it comes from, and how it is organized for proper and successful management. It is a big dataset! 

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://www.youtube.com/embed/4oM2ZY46ETA?si=B2jZYtS7Wb6iBWeL" title="A big data set" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>&nbsp;&nbsp;

### The WMO float identifier: a unique number for each float

Each one of the Argo floats has a unique identifier, known as the World Meteorological Organization float identifier, or just the WMO. The WMO identifier is assigned at the moment of the deployment of the float, but it is not hard-coded in the float.

### The basis of the Argo Data System

As explained in the videos of [Lesson 1- How the observations are done?](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter14_ObservationsDone.html#), when an Argo float surfaces, the data are received by one of the *Data Assembly Centers* (DAC). At the DACs, they are subjected to initial scrutiny using a set of real-time quality control tests where erroneous data are flagged or corrected, then the data are passed to one of the two Argo *Global Data Assembly Center* (GDAC), the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Monterey, California, USA). 

The GDACs are the first stage at which the freely available data can be obtained via the internet. The GDACs synchronize their data to ensure consistent data is available on both sites. The target is for these *real-time* data to be available within 12-24 hours of their transmission from the float.

Although in the Argo Online shcool we focus on the access to the primary source of the Argo data, additionally, Argo data can be accessed in several other ways:

- via the Global Telecommunication System for operational centers. 
- via interactive Data selection tools on the GDACs: the [US GDAC Data Browser](https://nrlgodae1.nrlmry.navy.mil/cgi-bin/argo_select.pl) and the [EuroArgo Selection Tool](https://dataselection.euro-argo.eu/)
- via [gridded fields and velocity products based on Argo](https://argo.ucsd.edu/data/argo-data-products/) NetCDF files from the GDACs.
- via data viewers that incorporate Argo data.
- via the [Global Argo Data Repository (GADR)](https://www.nodc.noaa.gov/argo/) for archived and offline data.
- via monthly copies of the GDACs https://www.seanoe.org/data/00311/42182/

See the [Argo data sources](https://argo.ucsd.edu/data/) at the Argo Steering team web page to read a full description, with links, to all these other ways of accessing the data.

#### Data organization at the GDAC

In the GDACS, the Argo data is organized in two different ways:

* By date, with one folder for each ocean basin, and then a folder for each year and month and a file for each day. 

* By DAC (data acquisition center) and Argo float (WMO number).

* By processing date: The last processed data organized by processing day, with access to the last 12 months.

At the early stage of the Argo program, and due to the huge amount of data that was foreseen Argo would create, it was decided that netCDF would be the official file format for the Argo data. 

In the [third lesson of the Argo Online school, Using Argo Data,](https://www.euro-argo.eu/argo-online-school/Lessons/L03_UsingArgoData/Chapter10_UsingArgoData_intro.html) we provide a hands-on python tutorial to understand the [netCDF format](https://www.euro-argo.eu/argo-online-school/Lessons/L03_UsingArgoData/Chapter11_TheNetCDFFormat.html) and how to [access Argo data by float](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter20_ArgoDatabyFloat_Intro.html) or [by date](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter30_ArgoDatabyDate_Intro.html).