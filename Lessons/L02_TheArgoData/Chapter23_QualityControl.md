# Quality control


#### Exhaustibe quality controls are needed

There are numerous reasons why data can be reported abnormally during the Argo profiler's operating cycles. It may be due to problems related to the CTD sensors, either external interference to the sensor, for instance, due to biodeposition, or intrinsic problems of the sensor itself. In both cases, incorrect data with spikes, biases, sensor drifts, etc., can be reported as bad data or possible bad data. Therefore Argo needs exhaustibe quality controls.

&nbsp;&nbsp;<center>
<iframe width="800" height="450" src="https://www.youtube.com/embed/pvJN-6OXtDw?si=0Br4TKIy4JNEkI-R&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>&nbsp;&nbsp;


#### The firtst quality control: Real-Time 

In real time, this is less than 24 hours since the data was measured by the Argo floats, a first Quality Control is carried out: the Real time Quality control (RTQC).

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/GIF_RT_QualityControl.gif" alt="Argo status" width="800"/></center>

Let's summarize this step:

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://www.youtube.com/embed/6GHUPfFHSNo?si=1fZfiZMBnJiQPYu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>&nbsp;&nbsp;

For instance, test 19 verifies whether the maximum pressure measured by a float is higher than the ocean depth in the location of the float; test 4 verifies if the location reported by the float is actually in the ocean, or if by error it is reporting a position overland; test 18 checks whether the float is sending, again and again, the same data, etc. We don’t expect you to learn what every test is about, but if you are curious about all of them, take a look at the [Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/), and here there is a list of the RTQC tests:

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/QC_Test.jpg" alt="Argo status" width="800"/></center>

*The full set of Argo Quality Control Manuals can be found here [ADMT Documentacion](http://www.argodatamgt.org/Documentation)*

All the data will be distributed in the Global Telecomunication Systrem (GTS), with its corresponding quality flags, that give an indication of the quality of the data. On the other hand, the data and its flags will be also converted to the netCDF format and sent to the Argo Global Data Management Centers (GDAC).

#### Problems in the sensors vs natural variability

However, detecting problems related to the CTD sensors can sometimes be very difficult. Even more when we take into account the concept of “natural variability”. Natural variability is just the natural change of the properties of the ocean and it may happen in periods ranging from seconds to millennia. For instance, changes occur daily, such as the tides; sporadically, such as storm surges or tsunamis; and seasonally, such as the simple warming of coastal waters in summer. In addition to the uncertainty associated with sensor errors, natural systems have an uncertainty associated with the range of natural variability itself. In such cases, it is very difficult to distinguish between the natural variability observed and the errors.

Since there is also natural variability in the temperature and salinity that can be mistaken for sensor malfunction, we have to be careful not to treat actual natural variability as sensor malfunction and correct it. 

For instance, a float may drift into saltier waters and we may misinterpret the change as sensor malfunctioning if we do not check out the trajectory of the float. It may also happen that an area of the ocean is becoming saltier than it used to be, and therefore if we compare the data with historical data, we risk losing this natural variability. 

Additionally thre are spikes, this is abrupt short changes in the data and constitute a clear case of anomaly. Spikes are easy to detect and correct. Drifts and offsets can be identified in the trend of ΔS over time, where ΔS is the difference in salinity between float-measured values and statistical recommendations. If ΔS = a + bt, where t is time, then a is the offset and b is the drift rate. Note that these drifts and offsets can be sensor-related, or they can be due to natural variability, as we explained before. To distinguish between sensor errors and natural variability evaluation it is necessary that experts look carefully at the data.

In the following figure, and video,  we show the most common behaviours found in the salinity data:

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/GIF_Bad_Data.gif" alt="Bad data" width="800"/></center>

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://www.youtube.com/embed/Ysq8G6JAESQ?si=xntH3TFHD-Nm6gGS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>&nbsp;&nbsp;


#### Biodeposition

Additionally Biodeposition could modify the shape of a sensor, as indicate in the following figure:

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/GIF_Biodeposition.gif" alt="Biodeposition" width="800"/></center>


Biodeposition is the small accumulations of organic matter, like the algae that grow in the pools in summer. It may affect the measurement’s accuracy by microscopic alterations of the sensor's shape. It mainly affects the conductivity sensors that allow us to measure salinity, and the effect of biodeposition is very small in most cases, but its effects on the data are approximate of the same order as the natural variations of the ocean in some regions. 

#### An additional quality control: The Delayed mode

Taking all of this into account, the Argo Comunity realized that RTQC was not enough and developed the Delayed mode Quality Control, when the data is compared with data from neighboring floats.  

&nbsp;&nbsp;<center><iframe width="800" height="450" src="https://www.youtube.com/embed/2AtB6ttgfBw?si=dVHzp5Kqq5Zj7H03" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>&nbsp;&nbsp;

Thus, one of the main obstacles since the start of the Argo Program was providing a technique that allowed us to distinguish between natural variations in salinity and the drift of the conductivity sensor due to biodeposition. The Delayed - Mode quality control is based on a statistical estimation called objective analysis; it provides a solid basis for interpolating irregularly spaced data. During the first years of the Argo era, researchers from the University of Washington and the Woods Hole Oceanographic Institution developed a method based on the comparison of all measurements of each Argo float and historical data at certain depth levels characterized by stability in salinity, but dependent on each zone. 

This method is known as OW (Wong et al, [Delayed-Mode Calibration of Autonomous CTD Profiling Float Salinity Data by θ – S Climatology](https://journals.ametsoc.org/view/journals/atot/20/2/1520-0426_2003_020_0308_dmcoac_2_0_co_2.xml)) calibration and is currently used for each of the floats. This type of calibration is repeated, at least, every year to guarantee the accuracy of the measurements. As we said before, this analysis is crucial to keeping measurements that don’t coincide with historical records but that contain natural variability unknown to date. Each data set must be carefully analyzed and, despite good tools such as objective analysis, the final decision on a possible data correction rests in the hands of the expert, what we call the Delayed Mode operator. 

In the following animation we show a real case of a Delayed mode calibration of salinity for float [6901268](https://fleetmonitoring.euro-argo.eu/dashboard?WMO=6901268) during its first 80 cycles (x-axis) . The blue line shows the actual measurements of the float at te isotherm 3.7C (around 2000 dbars) while the red line shows the value obtained by the OW method taking into account the nearby observations.

<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/GIF_DelayedMode.gif" alt="Delayed mode animation" width="800"/></center>

This is a clear case of sensor drift that was corrected (green line) during the Delayed Mode Quality Control, after the expert decision of the DM operator. 

To keep a record of all the actions performed, the data verified through the DM quality control will be marked with a "D" and those that have only been verified by the RT quality control will be marked with an "R":

- If the DM quality control has been performed after one year of data and the float is still active, both data collected in Real-Time "R" and data verified through DM quality control "D" will be available, being the latter the one with the highest quality.

- Once a float is declared as inactive, data will be collected in the GDAC as "D" and it will contain both adjusted and unadjusted data. 

Regardless of any changes done during the RT and DM quality controls, all the data is kept and included in the NetCDF files.

