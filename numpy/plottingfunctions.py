import time
import sys
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

def Plotvec1(u, z, v):

    ax = plt.axes() #generates full window axes
    ax.arrow(0,0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u') #adds the text u to the axes

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

Plotvec1(u, z, v)

#https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/jupyterlite/latest/lab/index.html?notebook_url=https%3A%2F%2Fcf-courses-data.s3.us.cloud-object-storage.appdomain.cloud%2FIBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork%2Flabs%2FModule%25205%2FPY0101EN-5-1-Numpy1D.ipynb