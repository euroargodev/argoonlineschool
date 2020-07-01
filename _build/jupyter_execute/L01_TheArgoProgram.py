#  Argo data

<img src="https://raw.githubusercontent.com/PedroVelez/argoonlineschool/master/images/logoArgo.png" alt="Argo status" width="50"/> Argo is a  broad-scale global array of profiling floats that measure temperature and salinity versus pressure. Argo is the major component of the ocean observing system. This is the actual distribution o the Argo array

<img src="http://www-hrx.ucsd.edu/www-argo/status.gif" alt="Argo status" width="700"/>


The objectives of Argo are:

- Provide a quantitative description of the changing state of the upper ocean and the patterns of ocean climate variability from months to decades, including heat and freshwater storage and transport.
- Enhance the value of the Jason altimeter through measurement of subsurface temperature, salinity, and velocity, with sufficient coverage and resolution to permit interpretation of altimetric sea surface height variability.
- Allow the initializing of ocean and coupled ocean-atmosphere forecast models, for data assimilation and for model testing.
- Document seasonal to decadal climate variability and to aid our understanding of its predictability. A wide range of applications for high-quality global ocean analyses is anticipated.

##  Why is it called Argo?
This questions is always in the mind of anyone than hears for the first time about the Argo program, therefore it is important to explain it. In Greek mythology, Argo was the ship in which Jason and the Argonauts sail to search for the golden fleece. In an analogus way, Argo floats sail the sea and complement the observations from the satellite called JASON-1, that measures the shape of the ocean surface.  Data from Argo and JASON-1 together will monitor the ocean currents, the oceans' transport of heat and freshwater around the globe and sea-level rise. 

Additionally, at the developing phase of the Argo network in 1998, a document prepared by Dean Roemmich of Scripps Institution of Oceanography, and entitled "A Proposal for Global Ocean Observations for Climate: the Array for Real-time Geostrophic Oceanography" explored the potential of using profiling floats to monitor the ocean, ... 

More information in the web page of the [Argo Steering Team](http://www.argo.ucsd.edu/index.html)

##  The netCF format
When an Argo float surfaces, the data are sent to the Argo Data System where they are processed and made available for everyone, free of charge. Here we describe the minimum neccesary information to understand and be able to use these data.

At the early stage of the Argo program, and due to the huge ammount of data that was foressen  Argo would create, it was decided that netCDF would be the offical file format for the argo data. In the next lesson we give an introduction to the properties of this data format, and how to read files in netCDF.

Before proceding, let's check if you really need this course, and try to answer the following questions:

- what is a WMO number ?
- what is the difference between Delayed and Real Time data mode ?
- what is an adjusted parameter ?
- what a QC flag of 3 means ?

If you don’t answer to more than 1 questions, please keep reading (or watching). Even though if you answered all the questions but you ara not very familiar with python, netCDF, or argopy,  you may find interesting the content of this course