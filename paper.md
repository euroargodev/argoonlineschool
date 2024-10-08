---
title: 'The Argo Online School: An e-learning tool to get started with Argo'
tags:
 - Jupyter Notebooks
 - Oceanography
 - Operational oceanography
 - Observing systems
 - Robotics
authors:
 - name: Alberto González-Santana^[co-first author]
   orcid: 0000-0001-5781-9330
   affiliation: 1
 - name: Pedro Vélez-Belchí^[co-first author]
   orcid: 0000-0003-2404-5679
   affiliation: 1
affiliations:
- name: Centro Oceanográfico de Canarias, Instituto Español de Oceanografía (IEO - CSIC)
  index: 1
date: 7 October 2024
bibliography: paper.bib
---

# Summary

The **Argo Online School (AoS)** is a set of videos, animations and hands-on python driven jupyter notebooks designed to make the data from the more than 4,000 profiling floats that constitute the Argo program, accessible. The Argo program samples, in near real time, the upper 2,000 meters of the ocean using a fleet of floats that drift with the ocean currents. The AoS consists of 28 chapters about the Argo program and its data, organized into a total of 3 lessons and 2 self-assessment sections:

* Lesson 1 is intended to introduce the basics of Argo, its objectives and key elements, such as the structure of the Argo floats and their operation in the open ocean.

* Lesson 2 focuses on the data coming from the Argo network, from its organization to its accessibility. Data quality control is also addressed through its two main modes: Real-Time and Delayed-Mode.

* Lesson 3 is the AoS hands-on component, and it requires basic knowledge of python. It offers a set of instructions to prepare a python environment in case the user wants to run the python Jupyter Notebooks on a local machine. This environment already includes recommended packages. The walk-through of Lesson 3 shows how to work with the netCDF format, how to access and process Argo data, and how to produce fancy plots for understanding information from Argo data.

The target audience of the AoS are high school, undergraduate or early graduate students, and the programming content included in Lesson 3 provides an ideal opportunity to support students with technical or science curriculum. Lessons 1 and 2 are themselves a closed module and could be used by a learner without using Lesson 3, assuming the goal is simply to learn about Argo.  It is recommended not to skip any lesson in the AoS as the content is carefully connected from lesser to greater complexity, providing a progressive learning experience. The user has the opportunity to self-assess the learning process carried out during their course in the AoS through interactive self-assessments.

The AoS has been designed to be expanded in the future to follow the implementation of new features in the Argo program.

# Statement of need

Argo [@roemmich-2019; @riser-2016] is an international program that collects information from inside the ocean using a fleet of floats that drift with the ocean currents. The floats move up and down between the surface and a mid-water level measuring ocean variables and spend almost all their life below the surface. Argo has been collecting more than 100,000 oceanographic profiles per year since 2012 and is composed of approximately 4,000 floats, constituting the major component of the [Global Ocean Observing System](https://www.goosocean.org/).

Although data from Argo [@Argo2021] is publicly and freely available, it is a huge dataset, with thousands of files and the free documentation is rather complex due to the many different models of floats and sensors and the need for traceability of the quality control of all the measurements. The Argo community has always been aware of the difficulties of new users to manage the complex and large datasets from the network. In that sense, the Argo Online School addresses an existing need for the Argo community to communicate on the Argo program and how its invaluable dataset can be used for various applications.

The potential of e-learning is used in the Argo Online School to offer all kinds of resources to users and thus promote and improve the access and use of the Argo data. In this way, the AoS is defined as an e-learning tool based on an interactive environment similar to other already established educational platforms. It is a tool with great educational potential that not only seeks to show the basic steps to use Argo data, but also to empower users so that they face future _programming_ scenarios in their academic and professional stage with confidence.

The AoS was presented at the [2nd Ocean Observers Workshop](https://bit.ly/3pUChmJ) on November 20th, 2021  and at the [22nd Argo Data Management Team meeting](https://bit.ly/3e39rLL) on December 10, 2021.

# Notes on instructional design

The AoS aims to teach the basic foundations to understand and use the Argo data. The AoS does not attempt to show everything about the Argo program, since the Argo documentation is available from the Argo Data Managment Team ([http://www.argodatamgt.org/Documentation](http://www.argodatamgt.org/Documentation)) [@ArgoManual2022, @ArgoQCManual2022] for deeper learning. The AoS is also not a library or Application Programming Interface to ease Argo data access, since there are other initiatives with that purpose; among others, *Argopy*, a python library for Argo data beginners and experts [@Maze2020] or  *ArgoVis*, a web application for fast delivery, visualization, and analysis of argo Data [@Argovis].

The AoS is a set of videos and hands-on python driven jupyter notebooks, designed to for high school, undergraduate or graduate students in any discipline, and it offers:

* An overview of the Argo program and an assessment of the need for Argo.
* A description of how the Argo data is organized.
* A description of how to access the Argo data.
* A description of the main characteristics of the Argo data format: the netCDF.
* A review of the main characteristics of the quality controls used: Real-Time and Delayed-Mode.
* Step-by-step instructions on data access, processing, and product generation, through the execution of commands based on the programming language python.

All content is divided into three lessons: 1. The Argo Program, that describes the basic concepts of this ocean observing network; 2. The Argo Data, that describes how the data is organized; and 3. Using the Argo data, that uses the knowledge of the previous sections and python driven jupyter notebooks to teach how to use the data. Finally, a quiz section is included for self-assessment.

Lessons 1 and 2 have been designed for students with knowledge similar to that acquired in high school, this is, basic knowledge about the relationships between the Earth’s processes, weather and climate; and basic skills in interpreting maps, charts, and tables to organize and analyze data. These two lessons are aimed at users with minimal or no knowledge of the Argo network, and itself are a closed module and could be used by a learner without using lesson 3, assuming the goal is simply to learn about Argo. Lessons 1 and 2 contain 32 short videos and 14 chapters and require about 5 hours to be completed. Lesson 3 is intended for advanced users, as it requires basic programming skills in python. However, Lesson 3 follows a step by step approach, to facilitate the transition of users coming from Lessons 1 and 2. The basic recommendations and instructions for configuring the hands-on section of the AoS are also provided, whether the users want to work online or if they want to work on their local computer. Specific python libraries and packages are recommended to guarantee the correct functioning of the AoS. Lesson 3 contains eight short videos and 14 chapters and requires about 10 hours to be completed, assuming basic knowledge of python.

The AoS has been developed using markdown, python driven Jupyter notebooks [@Kluyver2016jupyter] and jupyter-book [@JupyterBook2020], open source projects that allow editing control in a clear and easy way, and also permits web-based interactive development environments that contain code, visualizations, and texts. It is widely used for data science, and inspired by the course _[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html) [@Abernathey2021]. 

The AoS is accessible through the web page of Euro-Argo [https://www.euro-argo.eu/argo-online-school](https://www.euro-argo.eu/argo-online-school), but all the content that builds it is hosted in a public github repository: [https://github.com/euroargodev/argoonlineschool](https://github.com/euroargodev/argoonlineschool). As long as the Argo program continues to grow, the AoS will, too. This first version contains the basic content of Argo, subsequent versions will show the newest aspects of the Argo network, such as biochemical measurements, deep observations, etc. Anybody interested in helping to further develop the AoS may open and issue on the public github repository to begin to organize the update.

Given the structure of the AoS, it could be used for educational purposes. For high school students, Lessons 1 and 2 could be used as a project with the aim of finding science questions that ocean observations, such as Argo,  may help to understand, and how.  For students with a curriculum that includes programming in python, other projects could be to find the seasonal change in temperature at the surface at a given ocean, and compare it with the changes at 1,000 m or 2,000 m, or explain - sometimes is very hard- the trajectory of a given float.  Teachers are welcome to open an issue in the github repository to get help in how to develop more projects.

As part of the Argo community, the AoS follows the same philosophy in terms of data access, and to guarantee barrier-free learning: the information and data provided in the AoS is open access to the public and free of charge and therefore, no subscription is required.

# Acknowledgements

The AoS has been possible thanks to the collaboration of the Euro-Argo members, the Argo Steering Team ([https://argo.ucsd.edu](https://argo.ucsd.edu)) and has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE 824131 ([https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022)).

The audiovisual work has been recorded and edited by Rafael Méndez Pérez ([http://rafaelmendezp.com/](http://rafaelmendezp.com/)) while proofreading and english coaching support was provided by Agustín Prunell-Friend. The self-assessment sections are based on John M. Shea [@jmshea2021] software.

# References
