import numpy as np
import cv2
from imTriangle import triangle
import os

img_list = os.listdir('assets')
for img_fullname in img_list:
    print(img_fullname)
    img_fullname = f'assets/{img_fullname}'
    img_name, img_ext = os.path.splitext(img_fullname)
    
    img = cv2.imread(img_fullname)
    img_out = img.copy()
    
    [h, w, d] = img.shape
    for i in range(d):
        img_out[:, :, i] = triangle(img[:, :, i].copy(), coef=0.5)
    
    
        
    cv2.imwrite(f'{img_name}-triangled{img_ext}', img_out)



