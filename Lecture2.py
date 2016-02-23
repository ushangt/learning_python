
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1


# In[3]:

np.zeros((3,6))


# In[4]:

np.arrange(15)


# In[5]:

np.arange(15)


# In[6]:

np.arange(15,45)


# In[7]:

np.empty((2,3,2))


# In[12]:

for x in np.arange(1,50):
    if x%2 != 0:
        print(x)


# In[14]:

count = 0
for x in np.arange(1,50):
    if x%2 != 0:
        count = count + 1
np.zeros(count)


# In[15]:

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr = np.array(data1, dtype=np.int32)


# In[16]:

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr1 = arr + arr 
print(arr1)
print('---'*10)
arr * 5 


# In[18]:

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[:3, 1:]


# In[19]:

arr = np.arange(10)  
arr[arr.size-5:arr.size]


# In[20]:

arr


# In[21]:

arr[arr.size-5:arr.size] = 41


# In[22]:

arr


# In[23]:

arr + 1


# In[24]:

arr[arr >= 40] = 50


# In[25]:

arr


# In[29]:

for id, x in enumerate(arr):
    if id%5 == 0:
        print(x)


# In[31]:

zarr1 = [1,2, 3, 4,5,6, 7, 8, 9, 10,1,2, 3, 4,5,6, 7, 8, 9, 10,1,2,3,4,5]
zarr = np.array(zarr)
zarr.reshape((5,5))


# In[38]:

for j in range(5):
    for i in range(5):
        zarr[j][i] = j


# In[36]:

zarr


# In[ ]:



