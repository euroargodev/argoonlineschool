---
title: 'The Argo Online School (AOS): An e-learning tool to get started with Argo'
tags:
  - Jupyter Notebooks
  - Oceanography
  - Operational oceanography
  - Observing systems
  - Robotics
authors:
  - name: Alberto González Santana^[co-first author] 
    orcid: 0000-0001-5781-9330
    affiliation: 1 
  - name: Pedro Vélez Belchí^[co-first author]
    orcid: 0000-0003-2404-5679
    affiliation: 1
affiliations:
 - name: Instituto Español de Oceanografía (IEO - CSIC)
   index: 1
date: 23 December 2021
bibliography: paper.bib
---

# Summary
The **Argo Online School (AOS)** is a set of videos, animations and hands-on python driven jupyter notebooks designed to make the Argo program accessible for high school or graduate students in any discipline, with no prerequisites. It is integreatd by 25 sections about the Argo program and its data, organized into a total of 3  lessons and 2 self-assessment sections:

* Lesson 1 is intended to introduce the basics of Argo, its objectives and key elements such as the structure of the Argo floats and their operation in the open ocean.

* Lesson 2 focuses on the data coming from the Argo network, from its organization to its accessibility. Data quality control is also addressed through its two main modes: Real-Time and Delayed-Mode.

* Lesson 3 is the AOS hands-on component. It offers a set of instructions to prepare a python environment in case the user wants to run the python Jupyter Notebooks in a local machine. This environment already includes recommended packages, plus the last stable version of `argopy`, the python library for Argo data. The walkthrough of Lesson 3 shows how to work with the netCDF format, how to access and process Argo data, and how to produce fancy plots for understanding information from Argo data.

The target audience of the AOS are high school or early graduate students. The programming content included in Lesson 3 provides an ideal opportunity to support students in technical or science schools. It is recommended not to skip any lesson as the content is carefully connected from less to greater complexity, guaranteeing a progressive learning. The user has the opportunity to self-assess the learning process carried out during their course in the AOS through the proposed quizzes. 

The AOS has been designed to have the possibility to be expanded to following the implementation of new features in the Argo program.

# Statement of need

Argo [@roemmich-2019; @riser-2016] is an international program that collects information from inside the ocean using a fleet of floats that drift with the ocean currents. The floats move up and down between the surface and a mid-water level measuring ocean variables but spend almost all their life below the surface. Argo has been collecting more than 100,000 profiles per year since 2012, and nowadays Argo is composed by approximately 4,000 floats  and constitute the major component of the Global Ocean Observing System.

Although data from Argo are publicly and freely available, it is a huge dataset, with thousands of files and the free documentation is rather complex since it has to cope with the many different models of floats and sensors, and the trazability of the quality control of all the measurements. The Argo community has always been aware of the difficulties of early users to manage the complex and large datasets from the network. In that sense, the Argo Online School addresses an existing need for the Argo community to better communicate on the Argo programme and how its invaluable dataset can be used for various applications. 

The potential of e-learning platforms is used in the Argo Online School (AoS) to offer all kinds of resources to users and thus promote - improving access and use of Argo data. In this way, the AoS is defined as an e-learning tool based on an interactive environment similar to already established educational platforms. It is a tool with great educational potential that not only seeks to show the basic steps to use Argo data, but also to empower users so that they face future _programming_ scenarios in their academic and professional stage.

The AOS was presented at the [2nd Ocean Observers Workshop](https://bit.ly/3pUChmJ) on November 29th, 2021  and at the [22nd Argo Data Management Team meeting](https://bit.ly/3e39rLL) on December 10th, 2021.

# Notes on instructional design

<<<<<<< Updated upstream
The Argo online School aims to teach the basic foundations for Argo data understanding and using. The AOS does not attempt to show everything about the Argo program, since the Argo documentation is available for deeper learning. The AOS is a set of videos and hands-on python driven jupyter notebooks, designed to be accessible for high school or graduate students in any discipline, with no prerequisites. Specifically it offers:
=======
The audiovisual work has been recorded and edited by Rafael Méndez Pérez (http://rafaelmendezp.com/). Proofreading and coaching support by Agustín Prunell-Friend. Quiz sections are based on John M. Shea [@jmshea] work. 


The AOS has also been possible thanks to the collaboration of the Euro-Argo RISE members and the Argo Steering Team.
>>>>>>> Stashed changes

* An overview of the Argo program and an assessment of the need for Argo.
* A description of how the Argo data is organised.
* A description of how to access the Argo data.
* A description of the main characteristics of the Argo data format: the netCDF.
* A review of the main characteristics of the quality controls used: Real-Time and Delayed-Mode.
* Step-by-step instructions on data access, processing, and product generation, through the execution of commands based on a programming language.

<<<<<<< Updated upstream
All content is divided into 3 main lessons: 1. The Argo Program, that describes the basic concepts of the program, 2. The Argo Data  that describes the data is organised and  3. Using the Argo data,  that uses the knowledge of the previous sections and python driven jupyter notebooks teach how to use the data. Finally, a quiz section is included  for auto evaluation. Lessons 1 and 2 are aimed at users with minimal or no knowledge of the Argo network, therefore no prerequisites are needed. Lesson 3 is intended for advanced users, as it requires basic programming skills in python. However, lesson 3 is duly explained step by step, to facilitate the transition of users coming from lessons 1 and 2.  The basic recommendations and instructions for configuring the hand-on section of the AoS are also provided, whether the users want to work online or if they want to work on their local computer. Specific libraries and packages are recommended to guarantee the correct functioning of the AoS. To date, the three lessons contain a total of 25 sections, and all the sections have been carefully designed to be connected with the rest of the lessons.

The AOS has been developed using [@Kluyver2016jupyter] and [@JupyterBook2020], two open source projects that allow editing control in a clear and easy way, and also permits web-based interactive development environments that contain code, visualisations, and texts. It is widely used for data science, statistical modelling, and machine learning, among other disciplines. The AoS is inspided by the course _[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html)_ [@Abernathey2021] and is accessible through the web page of Euro-Argo [https://www.euro-argo.eu/argo-online-school](https://www.euro-argo.eu/argo-online-school). All the content that builds it up is hosted in the github repository of Euro-Argo: [https://github.com/euroargodev/argoonlineschool](https://github.com/euroargodev/argoonlineschool).

As long as the Argo program continues to grow, the AoS will, too. Although this first version contains the basic content of Argo, subsequent versions will show the newest aspects of the Argo network. As a product of the Argo community, the AOS follows the same philosophy in terms of data access. To guarantee barrier-free learning, the information and data provided in the AOS is available in open access to the public free of charge, therefore no subscription is required.

# Acknowledgements
=======
“These data were collected and made freely available by the International Argo Program and the national programs that contribute to it. (https://argo.ucsd.edu, https://www.ocean-ops.org). The Argo Program is part of the Global Ocean Observing System“

The Argo Online School has been funded by the European Union’s Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE [824131](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022)
>>>>>>> Stashed changes

The AOS has been possible thanks to the collaboration of the Euro-Argo RISE members, the Argo Steering Team ([https://argo.ucsd.edu](https://argo.ucsd.edu)) and has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE 824131([https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022)).

<<<<<<< Updated upstream
The audiovisual work has been recorded and edited by Rafael Méndez Pérez ([http://rafaelmendezp.com/](http://rafaelmendezp.com/)). Proofreading and english coaching support was provided by Agustín Prunell-Friend. The Quiz sections are based on John M. Shea [@jmshea2021]. 

# References
=======
>>>>>>> Stashed changes
