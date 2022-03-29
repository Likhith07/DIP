#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math                                               
import numpy as np
import cv2

image = cv2.imread(r"C:\Users\likuy\OneDrive\Desktop\messi.jpg")                                  #Reading the image 
a,b,c  = image.shape  

Increased_contrast = np.zeros(image.shape, image.dtype)           # Displaying increased contrast then original
Decreased_contrast = np.zeros(image.shape, image.dtype)           # Displaying image of increased contrast then original

High_Contrast_Control = 1.6   # controlling High Contrast
Low_Contrast_Control =  0.7      # controlling  Low Contrast
Brightness_Control = 0          # Controlling Brightness

for y in range(image.shape[0]):
    for x in range(image.shape[1]): 
        for c in range(image.shape[2]):
            Decreased_contrast[y,x,c] = np.clip(Low_Contrast_Control*image[y,x,c] + Brightness_Control, 0, 255) 
            Increased_contrast[y,x,c] = np.clip(High_Contrast_Control*image[y,x,c] + Brightness_Control, 0, 255)  #Clipping values out of range to into range

#Dispalying Images
cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.imshow("Contrast Increased Image", Increased_contrast)
cv2.waitKey(0)
cv2.imshow("Contrast Decreased Image", Decreased_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




