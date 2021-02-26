#!/usr/bin/env python
# coding: utf-8

# Name: Luz Ballesteros Gonzalez 

# Labpartner(s): Rocio 

# In[1]:


#import statements go here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Class 7.1

# Hope everyone is recovering from the freeze. Being in survival mode is stressful! I am going to attemt to be easy on you this week. As announced, there are no labs assigned last week, we are just taking a pass on those. I may have to shuffle some of the later material in the schedule, TBD.
# 
# I am having special office hours tomorrow, Tuesday 2-3 on the class zoom channel. I am asking those of you who are behind on any labs to check in with me and make a plan. If you can't make that time, let's schedule another one ASAP. Please note that you cannot miss these early labs and pass the class, and the material builds, so it is critical we get you caught up.
# 

# This week we are going to do more plotting, learn about functions, and apply this to your datasets. Next Monday we will have present your work day again, see below for details. Hopefully at this point the material is building to the point where it is not all forein and you will feel a bit more confident.
# 
# Originally we had introduction of Zotero and a CV assignment on the schedule for this week, but I'm pushing that until next week so we have less new material to deal with this week.

# # Warmups 7.1

# **W.1** Go through 1.4.1.5 Indexing and Slicking in the scipy lecture notes, up to the exercises, which you will do on Wednesday. http://scipy-lectures.org/intro/numpy/array_object.html#id2

# In[3]:


a = np.arange(10)


# In[4]:


a


# In[5]:


a[0], a[2], a[-1]


# In[6]:


#pythom idiom for reversing a sequence is supported:
a[::-1]


# In[7]:


#multidimensional arrays, indices are tuples of integers:
a = np.diag(np.arange(3))
a


# In[8]:


a[1,1]


# In[9]:


a[2,1] = 10 ## ['row', 'column'] by adding = it add it so third line, second colum added 10


# In[10]:


a


# In[11]:


a[1]


# In[12]:


## Arrays and other Python sequences can also be sliced
a = np.arange(10)
a


# In[13]:


a[2:9:3] # [start:end:step]


# In[14]:


a[:4]


# In[15]:


## three slice components are not required 
a[1:3] # started by default as 0 ended 1 and step 3


# In[16]:


a[::2]


# In[17]:


a[3:]


# In[19]:


## can also combines assingments and slicing 
a = np.arange(10)


# In[20]:


a[5:] = 10


# In[21]:


a ## changed the last 5 digits to 10


# In[22]:


b = np.arange(5)


# In[23]:


a[5:] = b[::-1]


# In[24]:


a ## added on position 5 the reverse of b 


# # Lecture 7.1
# 
# ### Agenda:
# 
# - The Parable Of Finding Nemo, or How To Do The Seemingly Impossible
# - Questions
# - Functions!
# 

# ### Questions

# In[ ]:





# In[ ]:





# ### Functions
# 
# Functions are super-useful for doing repetative tasks. You have been using pre-defined functions constantly, when you define arrays, make a plot, or analyse data. Now you are going to learn to write your own.
# 
# For more information on functions and documenting:
# - http://scipy-lectures.org/intro/language/functions.html?highlight=functions
# - https://realpython.com/documenting-python-code/
# 
# 
# Basic syntax:

# In[25]:


# first you define the function

def function_name():
    # some code that does something
    print('Inside the function')


# In[26]:


# then you call the function
function_name()


# Note that defined funtions show up using whos

# In[27]:


whos


# That's a really useless function, let's make a better one.

# In[28]:


# usually you want to pass a varible of some sort to the function to manipulate

def circle_area(radius):
    area = 3.14*radius**2
    return area   # the return statement means that the function will return that variable


# In[29]:


circle_area(5)


# What happens if I don't add the required input?

# In[30]:


circle_area() ## nothing because it's missing the positional argument 


# What happens if I omit the return statement?

# In[32]:


def circle_area2(radius):
    area = 3.14*radius**2
 


# How do I save the function output to a variable?

# In[34]:


circle_area2(5) ## Does not do anything just calculated inside


# Does the area variable inside the function exist outside of it?

# In[35]:


whos


# In[36]:


area ## what happens in the function stays in the function 


# Note I also could have made my function like this:

# In[41]:


def circle_area4(radius):
    return 3.14*radius**2


# In[38]:


circle_area4(5)


# In[43]:


my_circle_area = circle_area4(10)
my_circle_area


# ### Parsing for bad imput

# Note my above function will work even if the input is negative, which is not reasonable. So I probably want to include a statement that checks if the input is weird.

# In[58]:


def circle_area5(radius):
    if radius <= 0: 
        print('Error: radius needs to be positive')
        return # this exists the function 

    return 3.14*radius**2


# In[59]:


circle_area5(-3)


# In[60]:


circle_area5(0)


# In[55]:


circle_area5(3)


# ### Using packages within functions

# We can also have import statements within a function, but this can slow the function down if the package is not loaded already

# In[61]:


def circle_area6(radius = 3):
    import numpy as np
    
    return np.pi*radius**2


# In[62]:


circle_area6(3) # note this is a much more accurate


# In[63]:


circle_area6(3)


# We can have the function inputs have pre-defined default values, so that if you don't pass a variable it will use the default

# In[65]:


def circle_area7(radius = 3):
    import numpy as np #import numpy so we can use the more exact value of pi
    
    return np.pi*radius**2


# In[66]:


circle_area7() # no argument given, so uses radius = 3 by default


# Is numpy imported outside the function? Let's check

# In[70]:


np.pi


# In[68]:


# can our function handle lists? Let's check
r = [1,2,3]
circle_area7(r)


# In[69]:


# can our function handle arrays?

rnp = np.array(r)
circle_area7(rnp)

# what type of variable did the function return?


# ### It is very useful to add some documentation string info to your functions

# In[71]:


def circle_area7(radius = 3):
    """ Returns the area of a circle given the radius. 
    Assumes the radius is 3 if not supplied. """
    import numpy as np
    
    return np.pi*radius**2


# Now my note in the triple quotes shows up as a docstring

# In[73]:


get_ipython().run_line_magic('pinfo', 'circle_area7')


# There is a standard practice in programming to write out the Parameters (inputs/arguments) and Returns (output) in the docstring. Let's look a this for a predefined function and then make if for our simple function.

# In[74]:


get_ipython().run_line_magic('pinfo', 'np.pi')


# In[75]:


import numpy as np


# In[76]:


get_ipython().run_line_magic('pinfo', 'np.max')


# In[77]:


def circle_area7(radius = 3):
    """ Returns the area of a circle given the radius. 
    
    Parameters
    ----------
    radus: array like, radius of the circle
    Assumes the radius is 3 if not supplied.
    
    Returns
    -------
    area: ndarray or scalar
    Returns the area for the given radii
    
    """
    
    import numpy as np
    
    return np.pi*radius**2


# In[78]:


get_ipython().run_line_magic('pinfo', 'circle_area7')


# In[ ]:





# # Lab 7.1

# **E.1** Complete Introduction to Data Visualization with Matplotlib Chapters 1-2
# 

# In[ ]:


##completed


# **E.2** Make notes for yourself on progamming tecniques and commands you learned in the datacamp chapter above, including examples, comments and explainitory text. You can do this here or in a separate notebook that you link to here. Basically, you are making a cheat sheet for yourself.

# In[ ]:


## INTRO TO DATA VISUALIZATION WITH MATPLOTLIB
#pyplot interface
import matplotlib.pyplot as plt # import statement 
fig, ax = plt.subplots() # you can create subplots and select specific colums to plot
plt.show()


# In[ ]:


# Example from DataCamp 
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
# this if formatted as ax.ploy(x, y) and by doing ax.plot('Full data["column"]')


# In[ ]:


## you can also go ahead and put all together so plotting to sets of data 


# In[ ]:


## Custization tips and tricks 
ax.plot(x,y, color='color', marker = 'marker', linestyle = 'linestyle')
ax.set_xlabel('name')
ax.set_ylabel('name')
ax.set_title('title')


# In[ ]:


# Twin Axes 
ax2 = ax.twinx()
#annotate 
Ax.annotate ('text')


# ### This week's project:
# 
# For Monday's class you will write two functions that work on your dataset (you can use the same dataset or a different one). The first function will do some sort of analysis, manipulation or calculation, the second will be a plotting function. The idea here is that if you had another datafile that was similar, you could use the function to do the operation again easily.

# **E.3** Write one or more functions that manipulate your dataset and do some sort of analysis. You will present these to the class on Monday.

# In[99]:


import pandas as pd
data =  pd.read_csv('Soil_data.csv', index_col=0)
data
## not sure why the Unnamed happen.....


# In[101]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(data.index, data["pH"])
ax.set_xlabel("sample number");
ax.set_ylabel("pH");
ax.set_title("pH of Soil Samples")
plt.show()


# In[120]:


fig, ax = plt.subplots()
ax.plot(data.index, data["pH"], color="red")
ax2 = ax.twinx();
ax2.plot(data.index, data["ICP_Cd"], color="blue")
ax.set_xlabel("sample number");
ax.set_ylabel("pH", color = "red");
ax.set_title(" pH and Cd in Soil")
ax2.set_ylabel("Cd Concentration", color = "blue")
ax.tick_params('y', color="red")
ax2.tick_params('y', color="blue")
plt.show()


# In[122]:


def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)


# In[124]:


fig, ax = plt.subplots()
plot_timeseries(ax, data.index, data['pH'],'red','sample ID', 'pH') 

ax2 = ax.twinx()
plot_timeseries(ax2, data.index, data['ICP_Cd'],'blue', 'Sample ID', 'Cd Concentration (ppm)')

plt.show()


# **E.4** If you haven't yet, complete the introductions assignment on slack (add the channel, introduce yourself)

# In[ ]:


# completed

