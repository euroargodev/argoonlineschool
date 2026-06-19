##  The Argo data flow

The data flow is a representation to understand how the information moves through the system, from the early stages of data collection by the floats to their final disposal to the scientific community, operational services, and the general public. It is organized at different levels to guarantee its integrity and quality. Each level houses different centers that supervise the processes, contributing to the correct flow of data. Such is the case with the Argo Information Center (AIC), the National Data Acquisition Centers (DACs), the Global Data Acquisition Centers (GDAC), the Argo Regional Centers (ARC) and the different research centers. Do not worry about the acronyms! We are about to look at it carefully. 

Just imagine that these are necessary pieces in a gear system, that looks as the following diagram:

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/DataFlow.png" alt="Argo data flow" width="800"/></center>&nbsp;&nbsp;

When an **Argo float surfaces** (see the top of the diagram and follow the blue arrow), the data are received by one of the 11 *Data Assembly Centers*. 

The **Data Assembly Centers (DACs)** are the places where the raw data observed by Argo floats is processed and decoded into a well-defined data format. The data also undergoes a first quality control in real-time (Real-Time Quality Control) through initial scrutiny based on a certain number of tests, which allow its classification, making necessary corrections and discarding possible anomalous data.  Delivering the data within 12 to 24 hours of the transmission from the float is a basic requirement. In this way, the data is fully available to the scientific community and the general public at this stage. More information about quality control procedures will be provided in the following lessons.

After the data have been proceses in the DAC, are passed to one of the two Argo **Global Data Assembly Center (GDACs)**, the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Monterey, California, USA). Once in the GDACs, the data is made publicly available and can be obtained in netCDF format, free of charge through the internet. GDACs are also responsible for synchronizing with each other, to ensure the consistency and availability of the data on both sites. The data is also delivered, within the same 12 to 24 hours target, to the oceanic and climatic forecast operational centers via a different route, the Global Telecommunication System (GTS). In this case, this data is in a format called BUFR.

The next stage of the data flow only begins to operate about one year (1) after data is observed (seen the bottom of the diagram and follow the green arrow).  In this state, the intervention of expert scientific personnel is required to give a definitive boost in terms of the quality of the Argo data. There are numerous reasons why data can be reported abnormally during the Argo float's operating cycles. Studying the data, sometimes it is possible to discern between the natural variability of the area where the float is located and a possible sensor malfunction. Once the anomalous data and its causes have been determined, they can be corrected. This process is callled <u>Delayed Mode (DM) quality control</u>, and we'll look further into [Delayed Mode quality control](https://www.euro-argo.eu/argo-online-school/Lessons/L02_TheArgoData/Chapter14_RealTimeDelayedMode.html) later in the lesson. 

Once the data have gone through the Delayed mode quality control, it means that it has been inspected through a total of two exhaustive quality controls, guaranteeing the best quality and integrity of the data for the scientific community and the general public. Therefore (grre arrow)  the databases of DACs, GDACs, and ARCs will be updated a year later with the new data and the information of the status of each float will help the DAC to update the Real Time quality control.

An additional phase of Argo data flow is carried out at the **Argo Regional Centers (ARC)** that develop consistent regional datasets, to generate regional-specific analyses. This regional products will help the assessment of the Delayed Mode quality control. 


The **Argo Information Center (AIC)** oversees the processes to ensure that all the Argo floats are monitored.


###  All the data is saved

The “final data pool” is complemented with the inclusion of a historical climatological database worldwide. This database contains all the profiles collected by the Argo profilers in delayed mode and all the hydrographic profiles of those collected in selected oceanographic surveys. 


&nbsp;&nbsp;<center>
<iframe width="800" height="450" src="https://www.youtube.com/embed/hDhV80TB_QA?si=yEkEcxpBKwW-2KwA&amp;start=1" title="The Argo Online School 211 - The Argo data.  The Argo Data flow: All the data is saved" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

_The Argo Online School 211 - The Argo data. The Argo Data flow: All the data is saved_
&nbsp;&nbsp;