# What does a quality control flag mean?

Each data will have a specific quality flag assigned that indicates its status! Both Real-Time quality control and Delayed - Mode quality control follow a solid quality flag policy. Here we explain it, briefly:

&nbsp;&nbsp;<center>
<iframe width="800" height="450" src="https://www.youtube.com/embed/KEfgHYIcCo4?si=FMwLghCknsWOSvvS&amp;start=2" title="What does a quality control flag mean?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>&nbsp;&nbsp;

And here there are some examples that show how robust this quality flag policy is:

- The value assigned by a test cannot override a higher value from a previous test. Taking the Real-Time quality control as an example: a QC flag ‘4’ (bad data) set by Test 11 (gradient test) cannot be decreased to QC flag ‘3’ (bad data that is potentially correctable) set by Test 15 (gray list).
- A measurement with QC flag '4' (bad data) or '3' (bad data that are potentially correctable) cannot get a better QC flag in other quality control tests.
- Since salinity (PSAL) is almost always calculated from temperature (TEMP) and conductivity (CNDC), if the temperature is flagged '4' (or '3'), then salinity is also flagged as '4' (or '3').

The meaning of all the quality control flags use in Argo is in the folling table
<center><img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/QC_FLAGs.jpg" alt="Argo status" width="800"/></center>

from the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/)