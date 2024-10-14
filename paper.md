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
date: 14 October 2024
bibliography: paper.bib
---

# Summary

The **Argo Online School (AoS)** is a collection of videos, animations and hands-on python-driven jupyter notebooks designed to make the data accessible from more than 4,000 profiling floats that constitute the Argo program. The Argo program samples, in near real-time, the upper 2,000 meters of the ocean using a fleet of floats that drift with the ocean currents. The AoS consists of 28 chapters about the Argo program and its data, organized into a total of 3 lessons and 2 self-assessment sections:

* Lesson 1 is intended to introduce the basics of Argo, its objectives and key elements, such as the structure of the Argo floats and their operation in the open ocean.

* Lesson 2 focuses on the data coming from the Argo network, from its organization to its accessibility. Data quality control is also addressed through its two main modes: Real-Time and Delayed-Mode.

* Lesson 3 is the AoS hands-on component, and it requires basic knowledge of python. It provides a set of instructions for preparing a python environment in case the user wants to run the python Jupyter Notebooks on a local machine. This environment already includes recommended packages. The walk-through of Lesson 3 shows how to work with the netCDF format, how to access and process Argo data, and create visualizations to enhance understanding of the information derived from Argo data.

The target audience of the AoS is high school, undergraduate or early graduate students. The programming content in Lesson 3 offers an ideal opportunity to support students pursuing a technical or science curriculum. Lessons 1 and 2 form a closed module and can be used independently by learners who wish to focus solely on Argo. It is recommended not to skip any lesson in the AoS, as the content is carefully structured from simpler to more complex concepts, providing a progressive learning experience. Users have the opportunity to self-assess their learning progress through the proposed interactive self-assessments in the AoS.

The AoS has been designed to be expanded in the future to follow the implementation of new features in the Argo program.

# Statement of need

Argo [@roemmich-2019; @riser-2016] is an international program that collects information from inside the ocean using a fleet of floats that drift with the ocean currents. The floats move up and down between the surface and a mid-water level, measuring ocean variables, and spend almost their entire lifespan below the surface. Since 2012, Argo has collected over 100,000 oceanographic profiles per year and consists of approximately 4,000 floats, making it the major component of the [Global Ocean Observing System](https://www.goosocean.org/).

Although data from Argo [@Argo2021] is publicly and freely available, it represents a vast dataset with thousands of files. The accompanying documentation can be quite complex, as it must address the various models of floats and sensors, as well as the traceability of quality control for all measurements. The Argo community has always recognized the challenges faced by new users in managing the complex and extensive datasets from the network. In this context, the Argo Online School meets the need for effective communication about the Argo program and how its invaluable dataset can be utilized for various applications.

The Argo Online School leverages the potential of e-learning tools to provide a variety of resources to users, thereby promoting and enhancing access to and use of Argo data. In this way, the AoS is defined as an e-learning tool that offers an interactive environment similar to other established educational platforms. It is a tool with significant educational potential that aims not only to demonstrate the basic steps for using Argo data but also to empower users to tackle future _programming_ scenarios in their academic and professional careers with confidence.

The AoS was presented at the [2nd Ocean Observers Workshop](https://bit.ly/3pUChmJ) on November 20th, 2021  and at the [22nd Argo Data Management Team meeting](https://bit.ly/3e39rLL) on December 10, 2021.

# Notes on instructional design

The AoS aims to teach the fundamental concepts needed to understand and use Argo data. It does not seek to cover every aspect of the Argo program, as comprehensive documentation is available from the Argo Data Management Team ([http://www.argodatamgt.org/Documentation](http://www.argodatamgt.org/Documentation)) [@ArgoManual2022, @ArgoQCManual2022] for deeper learning. The AoS is also not library or Application Programming Interface to ease Argo data access, as other initiatives already fulfill that purpose, among others, *Argopy*, a python library for Argo data beginners and experts [@Maze2020] or  *ArgoVis*, a web application for fast delivery, visualization, and analysis of argo Data [@Argovis].

The AoS is a set of videos and hands-on python driven jupyter notebooks, designed for high school, undergraduate or graduate students in any discipline, and it offers:

* An overview of the Argo program and an assessment of the need for Argo.
* A description of how the Argo data is organized.
* A description of how to access the Argo data.
* A description of the main characteristics of the Argo data format: the netCDF.
* A review of the main characteristics of the quality controls used: Real-Time and Delayed-Mode.
* Step-by-step instructions on data access, processing, and product generation, through the execution of commands based on the programming language python.

All content is divided into three lessons: 1. The Argo Program, that describes the basic concepts of this ocean observing network; 2. The Argo Data, that describes how the data is organized; and 3. Using the Argo data, that takes the knowledge of the previous sections and python driven jupyter notebooks to teach how to use the data. Finally, a quiz section is included for self-assessment.

Lessons 1 and 2 are designed for students with knowledge comparable to that acquired in high school, this is, basic knowledge about the relationships between the Earth’s processes, weather and climate; and basic skills in interpreting maps, charts, and tables to organize and analyze data

These lessons are aimed at users with minimal or no knowledge of the Argo network, and itself are a closed module and could be used by a learner without using Lesson 3, assuming the goal is simply to learn about Argo. Lessons 1 and 2 contain 32 short videos and 14 chapters and require about 5 hours to completed. Lesson 3 is intended for advanced users, as it requires basic programming skills in Python.However, Lesson 3 follows a step by step approach, to facilitate the transition of users coming from Lessons 1 and 2. The basic recommendations and instructions for configuring the hands-on section of the AoS are also provided, whether the users want to work online or if they want to work on their local computer. Specific python libraries and packages are recommended to guarantee the correct functioning of the AoS. Lesson 3 contains 8 short videos and 14 chapters and requires about 10 hours to be completed, assuming basic knowledge of Python.

The AoS has been developed using markdown, python driven Jupyter notebooks [@Kluyver2016jupyter] and jupyter-book [@JupyterBook2020], open source projects that allow editing control in a clear and easy way, and also permits web-based interactive development environments that contain code, visualizations and texts. It is widely used for data science, and inspired by the course _[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html) [@Abernathey2021]. 

The AoS is accessible through the Euro-Argo webpage https://www.euro-argo.eu/argo-online-school, but all the content that makes it up is hosted in a public GitHub repository.: [https://github.com/euroargodev/argoonlineschool](https://github.com/euroargodev/argoonlineschool). As long as the Argo program continues to grow, the AoS will too.This first version contains the basic content of Argo; subsequent versions will showcase the newest aspects of the Argo network, such as biochemical measurements, deep observations and more. Anyone interested in helping to further develop the AoS may open an issue on the public GitHub repository to begin organizing the update.

Given the structure of the AoS, it could be used for educational purposes. For high school students, Lessons 1 and 2 could be a project to identify scientific questions that ocean observations, like those from Argo, may help address while developing essential know-how.  For students with a curriculum that includes programming in Python, other projects could involve finding the seasonal change in surface temperature at a specific ocean and comparing it with changes at 1,000 m or 2,000 m, or explaining the trajectory of a given float, which can be quite challenging.  Teachers are welcome to open an issue in the github repository to get assistance in how to develop new projects.

As part of the Argo community, the AoS follows the same philosophy regarding data access. To ensure barrier-free learning, the information and data provided in the AoS is open access to the public and free of charge and therefore, no subscription is required

# Acknowledgements

The AoS has been possible thanks to the collaboration of the Euro-Argo members, the Argo Steering Team ([https://argo.ucsd.edu](https://argo.ucsd.edu)) and has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE 824131 ([https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022)).

The audiovisual work has been recorded and edited by Rafael Méndez Pérez ([http://rafaelmendezp.com/](http://rafaelmendezp.com/)) while proofreading and english coaching support was provided by Agustín Prunell-Friend. The self-assessment sections are based on John M. Shea [@jmshea2021] software.

# References