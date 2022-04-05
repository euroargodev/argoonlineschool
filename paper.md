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
- name: Centro Oceanográfico de Canaarias, Instituto Español de Oceanografía (IEO - CSIC)
  index: 1
date: 1 April 2022
bibliography: paper.bib
---

# Summary

The **Argo Online School (AoS)** is a set of videos, animations and hands-on python driven jupyter notebooks designed to make the Argo program accessible. It is integrated by 25 sections about the Argo program and its data, organized into a total of 3  lessons and 2 self-assessment sections:

* Lesson 1 is intended to introduce the basics of Argo, its objectives and key elements, such as the structure of the Argo floats and their operation in the open ocean.

* Lesson 2 focuses on the data coming from the Argo network, from its organization to its accessibility. Data quality control is also addressed through its two main modes: Real-Time and Delayed-Mode.

* Lesson 3 is the AoS hands-on component. It offers a set of instructions to prepare a python environment in case the user wants to run the python Jupyter Notebooks in a local machine. This environment already includes recommended packages. The walkthrough of Lesson 3 shows how to work with the netCDF format, how to access and process Argo data, and how to produce fancy plots for understanding information from Argo data.

The target audience of the AoS are high school or early graduate students, and the programming content included in Lesson 3 provides an ideal opportunity to support students with technical or science curriculum. It is recommended not to skip any lesson in the AoS as the content is carefully connected from less to greater complexity, guaranteeing a progressive learning. The user has the opportunity to self-assess the learning process carried out during their course in the AoS through the proposed quizzes.

The AoS has been designed to have the possibility to be expanded to follow the implementation of new features in the Argo program.

# Statement of need

Argo [@roemmich-2019; @riser-2016] is an international program that collects information from inside the ocean using a fleet of floats that drift with the ocean currents. The floats move up and down between the surface and a mid-water level measuring ocean variables and spend almost all their life below the surface. Argo has been collecting more than 100,000 oceanographic profiles per year since 2012 and is composed of approximately 4,000 floats, constituting the major component of the [Global Ocean Observing System](https://www.goosocean.org/).

Although data from Argo [@Argo2021] is publicly and freely available, it is a huge dataset, with thousands of files and the free documentation is rather complex since it has to cope with the many different models of floats and sensors, and the traceability of the quality control of all the measurements. The Argo community has always been aware of the difficulties of early users to manage the complex and large datasets from the network. In that sense, the Argo Online School addresses an existing need for the Argo community to communicate on the Argo programme and how its invaluable dataset can be used for various applications.

The potential of e-learning platforms is used in the Argo Online School to offer all kinds of resources to users and thus promote and improve the access and use of the Argo data. In this way, the AoS is defined as an e-learning tool based on an interactive environment similar to other already established educational platforms. It is a tool with great educational potential that not only seeks to show the basic steps to use Argo data, but also to empower users so that they face future _programming_ scenarios in their academic and professional stage. 

The AOS was presented at the [2nd Ocean Observers Workshop](https://bit.ly/3pUChmJ) on November 20th, 2021  and at the [22nd Argo Data Management Team meeting](https://bit.ly/3e39rLL) on December 10, 2021.

# Notes on instructional design

The AoS aims to teach the basic foundations to understand and use the Argo data. The AOS does not attempt to show everything about the Argo program, since the Argo documentation is available from the Argo Data Managment Team ([http://www.argodatamgt.org/Documentation](http://www.argodatamgt.org/Documentation)) [@ArgoQCManual2022; @ArgoUserManual2021] for deeper learning. The AoS does not pretend to be a library or Application Programming Interface to ease Argo data access, since there are other initiatives with that purpose; among others, Argopy, a python library for Argo data beginners and experts [@Maze2020] or  ArgoVis, a web application for fast delivery, visualization, and analysis of argo Data [@Argovis].

The AoS is a set of videos and hands-on python driven jupyter notebooks, designed to be accessible for high school or graduate students in any discipline, with no prerequisites, and it offers:

* An overview of the Argo program and an assessment of the need for Argo.
* A description of how the Argo data is organized.
* A description of how to access the Argo data.
* A description of the main characteristics of the Argo data format: the netCDF.
* A review of the main characteristics of the quality controls used: Real-Time and Delayed-Mode.
* Step-by-step instructions on data access, processing, and product generation, through the execution of commands based on a programming language.

All content is divided into 3 lessons: 1. The Argo Program, that describes the basic concepts of this ocean observing network; 2. The Argo Data, that describes how the data is organized; and 3. Using the Argo data, that uses the knowledge of the previous sections and python driven jupyter notebooks to teach how to use the data. Finally, a quiz section is included for self-appraisal. 
Lessons 1 and 2 are aimed at users with minimal or no knowledge of the Argo network, therefore no prerequisites are needed. Lesson 3 is intended for advanced users, as it requires basic programming skills in python. However, lesson 3 is duly explained step by step, to facilitate the transition of users coming from lessons 1 and 2. The basic recommendations and instructions for configuring the hands-on section of the AoS are also provide, whether the users want to work online or if they want to work on their local computer. Specific libraries and packages are recommended to guarantee the correct functioning of the AoS. To date, the three lessons contain a total of 25 sections, and all the sections have been carefully designed to be connected with the rest of the lessons.

The AoS has been developed using python driven Jupyter notebooks [@Kluyver2016jupyter] and jupyter-book [@JupyterBook2020], two open source projects that allow editing control in a clear and easy way, and also permits web-based interactive development environments that contain code, visualizations, and texts. It is widely used for data science, and inspired by the course _[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html)_ [@Abernathey2021].  

The AoS is accessible through the web page of Euro-Argo [https://www.euro-argo.eu/argo-online-school](https://www.euro-argo.eu/argo-online-school), but all the content that builds it is hosted in the public github repository of Euro-Argo: [https://github.com/euroargodev/argoonlineschool](https://github.com/euroargodev/argoonlineschool).

As long as the Argo program continues to grow, the AoS will, too. This first version contains the basic content of Argo, subsequent versions will show the newest aspects of the Argo network, as biochemical measurements, deep observations, .. As part of the Argo community, the AOS follows the same philosophy in terms of data access, and to guarantee barrier-free learning, the information and data provided in the AoS is available in open access to the public free of charge and therefore no subscription is required.

# Acknowledgements

The AoS has been possible thanks to the collaboration of the Euro-Argo members, the Argo Steering Team ([https://argo.ucsd.edu](https://argo.ucsd.edu)) and has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE 824131 ([https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022)).

The audiovisual work has been recorded and edited by Rafael Méndez Pérez ([http://rafaelmendezp.com/](http://rafaelmendezp.com/)) while proofreading and english coaching support was provided by Agustín Prunell-Friend. The quiz sections are based on John M. Shea [@jmshea2021] software.

# References