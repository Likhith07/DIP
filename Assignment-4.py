#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2

image_original = cv2.imread('C:/Users/likuy/OneDrive/Desktop/messi.jpg')
image_reddish = cv2.imread('C:/Users/likuy/OneDrive/Desktop/messi.jpg')
image_greenish = cv2.imread('C:/Users/likuy/OneDrive/Desktop/messi.jpg')
image_blueish = cv2.imread('C:/Users/likuy/OneDrive/Desktop/messi.jpg')

image_blueish[:,:,1],image_blueish[:,:,2] = 0,0
image_greenish[:,:,0],image_greenish[:,:,2] = 0,0           
image_reddish[:,:,-2],image_reddish[:,:,0] = 0,0

cv2.imshow("Original Image",image_original)
cv2.waitKey(0)
cv2.imshow("Reddish Image",image_reddish)
cv2.waitKey(0)
cv2.imshow("Greenish Image",image_greenish)
cv2.waitKey(0)
cv2.imshow("Blueish Image",image_blueish)
cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:




