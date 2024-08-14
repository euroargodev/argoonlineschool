# Accesing the Argo data

#### how is the data organized?

Let's see how the Argo data is organized in different folders in the GDACs:

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://drive.google.com/file/d/1Ld73L9nTlebGpOdepRTDA3e5UwzPwQse/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


#### What is FTP?

But how we can actually get the data?:

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://drive.google.com/file/d/1Mbfk07QANv4Jm7ZMTWbwNtbBxFcaemRM/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


#### Using FTP or HTTPs

To access the data directly from the GDACs we can use the FTP or HTTPs protocols. Although it sound complex is very easy:

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://drive.google.com/file/d/1YV1ZJajaPf0dh4KyvRx70dqTiWPdxVI0/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

This are the address:

##### FTP
- [US GDAC ftp://usgodae.org/pub/outgoing/argo](ftp://usgodae.org/pub/outgoing/argo)
- [EU GDAC ftp://ftp.ifremer.fr/ifremer/argo](ftp://ftp.ifremer.fr/ifremer/argo)

##### HTTPs
- [US GDAC https://data-argo.ifremer.fr](https://data-argo.ifremer.fr)
- [US GDAC https://usgodae.org/pub/outgoing/argo)](https://usgodae.org/pub/outgoing/argo)


#### A FTP hands-one example

Take a look at this simple example on how to get access to Argo data through Coriolis GDAC FTP. Let's go for it!

1. Before opening the FTP client, make sure where the files are allocated. In this case, the files are located in ftp.ifremer.fr/ifremer/argo.
2. Open the FTP client and fill in the box with the host provided ftp.ifremer.fr/ifremer/argo in the host.
3. You are now connected to the Coriolis GDAC!

&nbsp;&nbsp;<center>
<iframe width="800" height="450" src="https://drive.google.com/file/d/1Ct71C4wFOTvaL-J_oEUXa2-_rbYJmRKi/preview" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

Each data will have a specific quality flag assigned that indicates its status! Both Real-Time quality control and Delayed - Mode quality control follow a solid quality flag policy. Here are some examples that show how robust this quality flag policy is:

• The value assigned by a test cannot override a higher value from a previous test. Taking the Real-Time quality control as an example: a QC flag ‘4’ (bad data) set by Test 11 (gradient test) cannot be decreased to QC flag ‘3’ (bad data that is potentially correctable) set by Test 15 (gray list).

• A measurement with QC flag '4' (bad data) or '3' (bad data that are potentially correctable) cannot get a better QC flag in other quality control tests.

• Since salinity (PSAL) is almost always calculated from temperature (TEMP) and conductivity (CNDC), if the temperature is flagged '4' (or '3'), then salinity is also flagged as '4' (or '3').

#### HTTPs is easy

Although HTTPs sounds very technical, we are used to it:

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://drive.google.com/file/d/1qATH7z-qrCQ4FrzFfG_gSeuqypneiqys/preview" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


#### Others ways to access the data

Additionally to the HTTP and FTP ways of accessing the data, there are resources such as "data viewers" which allow us to obtain useful information from the data in an easy way.

There are almost ten Argo data viewers, some with more features than others. In the next video we will quickly check how the [Euro - Argo data viewer](https://fleetmonitoring.euro-argo.eu/) works 


&nbsp;&nbsp;<center><iframe width="800" height="450"  src="https://drive.google.com/file/d/1zFAYzYkMlH50DR1RfLfmacVAU4I8_Cpm/preview" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


#### The data selection tool

Nowadays, some data viewers have added extremely useful technical developments to fine-tune users' searching for Argo data. This is the case of the new [Argo data selector](dataselection.euro-argo.eu) developed under the framework of the Euro Argo RISE project (EARISE) . As you can check, its interface is very similar to the previous [Euro - Argo data viewer](https://fleetmonitoring.euro-argo.eu/) but it includes some new features. 


&nbsp;&nbsp;<center>
<iframe width="800" height="450"  src="https://drive.google.com/file/d/135pKPNA8PLb9UOsucJWRdE4762ha_x4W/preview" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


The [Argo data selector](dataselection.euro-argo.eu) is user friendly and developped focused in a interactive selection:

&nbsp;&nbsp;<center>
<iframe width="800" height="450" src="https://drive.google.com/file/d/13uquh52TEOF2jO6PF_9EsocKD83odbJr/preview" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>