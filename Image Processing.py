#!/usr/bin/env python
# coding: utf-8

# # Image Processing - Inverting the Image Colour
# -------------------------------------------------------------------------------------------------------------------------------
# For this demonstration I'll use the **python imaging library `(PIL)` and a function to display images in the Jupyter notebook**

# In[1]:


import numpy as np
from PIL import Image
from IPython.display import display


# And let's just look at the image I'm talking about

# In[2]:


im = Image.open("JustForFun.jpg")
display(im)


# Now, we can conver this `PIL` image to a `numpy` array

# In[3]:


im_array = np.array(im)
print("Shape of im_array : ", im_array.shape)
im_array #prints the whole im_array


# Here we see that we have a `(1280, 719, 3)` 3 - D array and that the values are all `uint8`. The `uint` means that they are
# **unsigned integers** (so no negative numbers) and the 8 means 8 bits per byte. This means that each value can
# be up to *2*2*2*2*2*2*2*2=256* in size **(well, actually 255, because we start at zero)**. For black and white
# images black is stored as 0 and white is stored as 255. So if we just wanted to invert this image we could
# use the numpy array to do so

# In[4]:


all_black_array = np.ones((1280, 719, 3)) * 255
print("Shape of im_array : ", all_black_array.shape)
all_black_array #prints the whole all_black_array


# Now let's subtract that `im_array` from the `all_black_array`

# In[5]:


inv_im_array = im_array - all_black_array


# Let's display the `inv_im_array` for experimentation

# In[6]:


print("Shape of inv_im_array : ", inv_im_array.shape)
inv_im_array #prints the whole all_black_array


# From the output of the above code cell we can say that the shape of the `inv_im_array` is matched to `im_array` but the array elements in `inv_im_array` **are negative valuse which can't be used for image processing**.
# 
# So, let’s multiply the `inv_im_array` with `-1` to change the array elements in `inv_im_array` to a positive value.

# In[7]:


inv_im_array = inv_im_array*-1


# And as a last step, let's tell `numpy` to set the value of the datatype to `uint8`

# In[8]:


inv_im_array = inv_im_array.astype(np.uint8)


# In[9]:


print("Shape of inv_im_array : ", inv_im_array.shape)
inv_im_array


# Now everthing looks perfect and now we can display the `inv_im_array` as image using `PIL` module.

# In[10]:


display(Image.fromarray(inv_im_array))


#                                      Thank You !!!                           
# 
#                          --------------The End----------------
