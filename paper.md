---
title: 'The Argo Online School (AOS): An e-learning tool to get started with Argo'
tags:
  - Jupyter Notebooks
  - Oceanography
  - Operational oceanography
  - Observing systems
  - Robotics
authors:
  - name: Alberto González Santana^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0001-5781-9330
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Pedro Vélez Belchí^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0003-2404-5679
    affiliation: 1
affiliations:
 - name: Instituto Español de Oceanografía (IEO - CSIC)
   index: 1
date: 23 December 2021
bibliography: paper.bib
---

# Summary

The **Argo Online School (AOS)** tool is a set of Jupyter Notebooks, consisting of more than "20 sections" about Argo and its data, integrated into a total of 3 "core" lessons and 2 self-assessment sections. 

* Lesson 1 is intended to introduce the basics of Argo, its objectives and key elements such as the structure of the Argo floats and their operation in the open ocean.

* Lesson 2 focuses on the data coming from the Argo network, from its organization to its accessibility. Data quality control is also addressed through its two main modes: Real-Time and Delayed-Mode.

* Lesson 3 is the AOS hands-on component. It offers a set of instructions to prepare a python environment in case the user wants to run the python Jupyter Notebooks in a local machine. This environment already includes recommended packages, plus the last stable version of `argopy`, the python library for Argo data. The walkthrough of Lesson 3 shows how to work with the netCDF format, how to access and process Argo data, and how to produce fancy plots for understanding information from Argo data.

It is recommended not to skip any lesson as the content is carefully connected from less to greater complexity, guaranteeing a progressive and safe learning. The user has the opportunity to self-assess the learning process carried out during their course in the AOS through the proposed quizzes. The target audience of the AOS are high school or early graduate students. Technical or scientific education programs are an advantage to address the programming content included in lesson 3. 

# Statement of need

Argo is a large-scale global array of approximately 4,000 floats that collect physical and biogeochemical data from the ocean. Although data from Argo are publicly and freely available, the Argo community has always been aware of the difficulties of users to manage the complex and large datasets from the network. Their main uncertainties are mainly focused on obtaining the Argo data, its processing through base codes  and the generation of products to interpret the information contained in the datasets. 

The potential of e-learning platforms is used to offer all kinds of resources to users and thus promote - improving access and use of Argo data. In this way, the Argo Online School (AOS) is defined as an e-learning tool based on an interactive environment similar to already established educational platforms. It is a tool with great educational potential that not only seeks to show everything about Argo, but also to empower users so that they face future _programming_ scenarios in their academic and professional stage. 

As long as the Argo program continues to grow, the AOS will, too. Although this first version contains the basic content of Argo, subsequent versions will show the newest aspects of the Argo network. As a product of the Argo community, the AOS follows the same philosophy in terms of data access. To guarantee barrier-free learning, the information and data provided in the AOS is available in open access to the public free of charge, therefore no subscription is required. The AOS is accessible through the web page of Euro-Argo (https://www.euro-argo.eu/argo-online-school), but all the content that builds up the web page is hosted in the github repository of Euro-Argo:  https://github.com/euroargodev/argoonlineschool. 

The AOS was presented at the [2nd Ocean Observers Workshop](https://bit.ly/3pUChmJ) on November 20th, 2021  and at the [22nd Argo Data Management Team meeting](https://bit.ly/3e39rLL) on December 10, 2021.

# Acknowledgements

The audiovisual work has been recorded and edited by Rafael Méndez Pérez (http://rafaelmendezp.com/). Proofreading and coaching support by Agustín Prunell-Friend. Quiz sections are based on John M. Shea [@jmshea](https://github.com/jmshea) work. The AOS has also been possible thanks to the collaboration of the Euro-Argo RISE members and the Argo Steering Team. Other learning tools based on this design pattern include the _Earth and Environmental Data Science_ (https://github.com/earth-env-data-science/earth-env-data-science-book), which inspired the creation of the AOS. 

Since data are freely available without restriction, to track uptake and impact, we ask that where Argo data are used in a publication or product, an acknowledgement be given. To acknowledge Argo, please use the following sentence and the appropriate Argo DOI afterward as described below.

“These data were collected and made freely available by the International Argo Program and the national programs that contribute to it. (https://argo.ucsd.edu, https://www.ocean-ops.org). The Argo Program is part of the Global Ocean Observing System“.

The Argo Online School has been funded by the European Union's Horizon 2020 research and innovation program under grant agreement Euro-Argo RISE [824131](https://www.euro-argo.eu/EU-Projects/Euro-Argo-RISE-2019-2022).

# References

- Owens, W. B. & Wong, A. P. S. An improved calibration method for the drift of the conductivity sensor on autonomous CTD profiling floats by θ–S climatology. Deep Sea Research Part I: Oceanographic Research Papers 56, 450–457 (2009). Retrieved from https://doi.org/10.1016/j.dsr.2008.09.008.
- Riser, S. C. et al. Fifteen years of ocean observations with the global Argo array. Nature Clim Change 6, 145–153 (2016). Retrieved from https://doi.org/10.1038/nclimate2872
- Roemmich, D. et al. The Argo Program: Observing the Global Oceans with Profiling Floats. Oceanog. 22, 34–43 (2009). Retrieved from https://doi.org/10.5670/oceanog.2009.36
- Wong, A. P. S. et al. Argo Data 1999–2019: Two Million Temperature-Salinity Profiles and Subsurface Velocity Observations From a Global Array of Profiling Floats. Front. Mar. Sci. 7, 700 (2020). Retrieved from https://doi.org/10.3389/fmars.2020.00700
- Argo Steering Team https://argo.ucsd.edu/ 
- Argo Data Management Team http://www.argodatamgt.org/
- Euro - Argo https://www.euro-argo.eu/ 