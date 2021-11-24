#!/usr/bin/env python
# coding: utf-8

# ## How the observations are done?

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<center>\n<iframe width="560" height="315" src="https://drive.google.com/file/d/1hpaqZYzF2BFGUSnA0IPialFfQNfw6q6q/preview" width="640" height="480" title="The Argo Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</center>')


# Vídeo [104-02]

# ### **What’s inside an ARGO float?**
# 
# The standard Argo floats are devices of about 20 kg weight and roughly 2 meters height. They dive vertically by changing their buoyancy via an inflatable external bladder, so it can surface and dive. There is no propulsion system at all, so its horizontal displacements are performed by letting itself be carried by the currents. It consists of three subsystems [pointing out the float].
#  
# **Hydraulic System:** controls the buoyancy through an external inflatable bladder so that the profiler can resurface and submerge. An Argo float's critical capacity is its ability to rise and sink in the ocean in the scheduled time. Profilers do this by changing their effective density. Density is the mass of an object divided by its volume. The Argo float keeps its mass constant but, by altering its volume, it changes its density. To do this, mineral oil is forced out of the float's pressure case and expands a rubber bladder at the bottom end of the float. As the bladder expands, the float becomes less dense than seawater and rises to the surface. Upon finishing its tasks at the surface, the float withdraws the oil and descends again.
# 
#  
# **Microprocessors:** The electronics include a microprocessor that stores the data from the sensors until it can be transmitted, a program that controls when the float sinks and rises and a position-fixing and data-transmission system that controls the interaction with the satellite. Each float has a unique number that allows it to be recognized and distinguished from all the other floats.
# 
#  
# **Data Transmission System:** controls communication with satellites. For the monitoring and control of the Argo array of floats, two communication systems are fundamentally used: ARGOS and Iridium. As the float ascends, the  data collected is stored in itself. When the float reaches the surface, the data is transmitted to the satellites.
# 
# The satellite communication systems related to the Argo floats use satellites that “orbit” around the Earth. The orbital communication satellites move inside an orbit so that the satellite passes above a particular geographic location at regular intervals. The ARGOS system is served by 7 polar-orbiting satellites at an altitude of 850 km and completes a revolution around Earth approximately every 100 minutes. With the first Argos unidirectional system, the floats needed 6-10 hours at the surface to be able to transmit the collected data. The newest version, called the Argos-3 system, allows floats to transmit data in just a few minutes.
#  
# On the other hand, the Iridium system has 66 satellites at a height of approximately 781 km. Iridium is the largest commercial satellite constellation in the world and, approximately 80% of Argos’s floats transmit their data via the Iridium system. The design of the Iridium network allows “data calls” to be relayed from one satellite to another until they reach the satellite that registers the float concerned, and the signal is then relayed back to Earth. The IRIDIUM system requires only “minutes” to transfer the floats’ information to the receiving stations. Data transfer between the float and the satellites is possible thanks to a unique 12-digit Identification Number, which is associated with the float.
# 

# In[ ]:




