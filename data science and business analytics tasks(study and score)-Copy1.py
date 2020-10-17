#!/usr/bin/env python
# coding: utf-8

# # GRIP at  the sparks foundation
# 
# 
# # name = shivam prajapati
# 
# 
# # task 2 = Data Science  & Business Analytics Tasks
# 
# 

# In[1]:


#import the library which is useful 
import pandas as po
from scipy import stats         #for all element of regrassion
import matplotlib.pyplot as plt  #for plotting and visulation 


#our data loaction and read it in a

print("our data \n")
a=po.read_csv("http://bit.ly/w-data")
print(a)


# In[2]:


#slope and all the related segment of this

slope,intercept ,r, p, std_err=stats.linregress(a.Hours,a.Scores)

def myfunc(x):
   return slope * x + intercept


#draw mapping line or point idntified one place

print(" \n\n draw mapping line")
mymodel = list(map(myfunc, a.Hours))

#final flotting

plt.scatter(a.Hours,a.Scores)
plt.plot(a.Hours,mymodel)
plt.show()



print("your result for study 9.25 hour is")

myfunc(9.25)
   


# In[ ]:




