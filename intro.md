<p align="center">
   <img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoAoS_banner.png" alt="AoS logo" width="600"/>
</p>

[![status](https://jose.theoj.org/papers/b66eaed8751b3adb6f2f4ad146380818/status.svg)](https://jose.theoj.org/papers/b66eaed8751b3adb6f2f4ad146380818)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13929139.svg)](https://doi.org/10.5281/zenodo.13929139)

# The Argo Online School

[Argo](https://argo.ucsd.edu/) is an international program that collects information from inside the ocean using a fleet of approximately 4,000 floats that drift with the ocean currents. The floats move up and down between the surface and a mid-water level, measuring ocean variables, but spend almost all their life below the surface. The following figure shows the actual configuration of the Argo fleet:

<figure>
<img src="http://sio-argo.ucsd.edu/statusbig.gif" alt="Argo status" width="800"/>
<figcaption>Actual status of the Argo fleet</figcaption>
</figure>

Argo has been collecting more than 100,000 profiles per year since 2012, and nowadays Argo is the major component of the [Global Ocean Observing System](https://goosocean.org/).

Given the amount of data gathered by the Argo network of floats, the associated documentation has grown considerably and can be overwhelming. That's why we developed the Argo Online school **AoS**, to teach the basic foundations to use and understand the Argo data. The AoS is a set of guided-short videos and hands-on jupyter notebooks designed for high school or graduate students in any discipline.
The AoS is organized in two parts. The fist one, with two lessons, is devoted to teaching what is the The Argo Program and The Argo Dataset, with a set of 32 short videos and 14 chapters. Lessons 1 and 2 have been designed for students with knowledge similar to those acquired to get into high school, this is, basic knowledge about the relationships between the Earth’s processes, weather and climate; and basic skills in interpreting maps, charts, and tables to organize and analyze data. These two lessons are themselves a closed module, assuming the goal is simply to learn about Argo.
The second part includes only one lesson: Using the Argo data, with jupyter notebooks and 8 short videos to teach, hands-on in 14 chapters, how to access the Argo data and use it. This lesson has been designed for students with knowledge similar to those necessary for lesson 1 and 2 and basic knowledge of the programming language python.

Lessons 1 and 2 require about 5 hours to be completed, while lesson 3 requires 10 hours to be completed, assuming basic knowledge of python.

These are the chapters in each lesson:

**Lesson 1. [The Argo Program](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter10_TheArgoProgram_intro.html)**

In this section and using a set of videos you will learn about:
* [What is the Argo network?](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter11_WhatArgoNetwork.html)
* [Why Argo?](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter12_NeedArgo.html)
* [How the observations are done?](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter13_ObservationsDone.html)
* [What is an oceanographic profile?](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter14_OceanographicProfile.html)
* [Technological innovations](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter15_TechInnovations.html)
* [Recap](https://euroargodev.github.io/argoonlineschool/Lessons/L01_TheArgoProgram/Chapter16_RecapLesson1.html)

**Lesson 2. [The Argo Data](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter10_TheArgoData_intro.html)**

In this section and using a set of videos you will learn about:
* [The Argo General Data Stream](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter12_ArgoDataStream.html)
* [What are the Argo data and its format?](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter13_WhatArgoDataFormat.html)
* [QualityControl](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter14_QualityControl.html)
* [What does a quality control flag mean?](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter15_QualityFlagMean.html)
* [Accesing the Argo data](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter16_GetAccesOrganized.html)
* [Recap](https://euroargodev.github.io/argoonlineschool/Lessons/L02_TheArgoData/Chapter17_RecapLesson2.html)

Additonally we have included Quizzes for the [first](https://euroargodev.github.io/argoonlineschool/Lessons/Quizzes/Quiz10.html) and [second](https://euroargodev.github.io/argoonlineschool/Lessons/Quizzes/Quiz20.html) lessons if you want to challenge yourself!

**Lesson 3. [Using the Argo data](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter10_UsingArgoData_intro.html)**

In this section and using hands-on jupyter notebooks you will learn about:
* [The netCDF format](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter31_TheNetCDFFormat.html)
* [Accesing Argo data by float](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter32_ArgoDatabyFloat_Intro.html)
* [Accesing Argo data by date](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter33_ArgoDatabyDate_Intro.html)
* [Accesing Real-Time and Delayed mode data](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter34_RTandDM.html)
* [Additional examples](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter36_Examples.html)
* [Recap](https://euroargodev.github.io/argoonlineschool/Lessons/L03_UsingArgoData/Chapter35_RecapLesson3.html)

Given the structure of the AoS, it could be used for educational purposes. For high school students, lessons 1 and 2 could be used as a project with the aim of finding questions that ocean observations, such as Argo,  may help to understand, and how.  For students with a technical or science curriculum, that includes programming in python, other projects could be to find the seasonal change in temperature at the surface at a given ocean, and compare it with the changes at 1000 m or 2000 m, or explain - sometimes is very hard- the trajectory of a given float.  Teachers are welcome to open an [issue on the public github repository](https://github.com/euroargodev/argoonlineschool/issues) to get help in how to develop more projects.

## Further reading

The AoS does not attempt to show everything about Argo, since the Argo documentation is available for deeper learning. More information about the Argo network can be found in the [Argo Steering Team web page](http://www.argo.ucsd.edu/), the [Argo Data Management team documentation](http://www.argodatamgt.org/Documentation) or the European contribution to Argo: [Euro-Argo](https://www.euro-argo.eu/). Specifically the [Argo user’s manual](https://archimer.ifremer.fr/doc/00187/29825/) and the [Argo Quality Control Manual for CTD and Trajectory Data](https://archimer.ifremer.fr/doc/00228/33951/) are the nexts steps to go deeper in the advance use of Argo data.

## Acknowledging Argo data

Since Argo data are freely available without restriction, to track uptake and impact, we ask all users to acknowledge it in the following way:*“These data were collected and made freely available by the International Argo Program and the national programs that contribute to it.  (https://argo.ucsd.edu,  https://www.ocean-ops.org).  The Argo Program is part of the Global Ocean Observing System“*
s
Additionally, the Argo Data Management Team assigns Digital Object Identifiers (DOIs) to Argo documents and datasets. These can easily be included in publications and keep a direct and permanent link to the Argo document or datasets used in publications (to ensure reproducibility). Datasets are archived in [monthly snapshots each with its own DOI](https://www.seanoe.org/data/00311/42182/).

Refer to [How to cite Argo data](https://argo.ucsd.edu/data/acknowledging-argo/) for further information.

## License for this book

All the content in the Argo Online School is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0) license.

## How to contribute

As long as the Argo program continues to grow, the AoS will, too. This first version contains the basic content of Argo, subsequent versions will show the newest aspects of the Argo network, such as biochemical measurements, deep observations, etc. Since all the content that builds the Argo online school is hosted in a public github repository: [https://github.com/euroargodev/argoonlineschool](https://github.com/euroargodev/argoonlineschool), anybody interested in helping to further develop the AoS may open an [issue on the public github repository](https://github.com/euroargodev/argoonlineschool/issues) to begin to organize the update.

## Credits

The Argo Online School has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement [Euro-Argo RISE 824131](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022). The video production has been done by [Rafael Luis Mendez Peña](http://rafaelmendezp.com/). Quiz sections are based on [John M. Shea](https://github.com/jmshea) work. The AOS has also been possible thanks to the collaboration of the Euro-Argo RISE members and the [Argo Steering Team](https://argo.ucsd.edu/organization/argo-steering-team/).