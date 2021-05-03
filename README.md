# imTriangle
This snippet of code attempts to put triangle pixelation effect on images.

## Installation

Run the following to install:

```python
pip install imTriangle
```

## Usage
```python
import cv2
import numpy as np
from imTriangle import triangle

img_fullname = 'assets/lotus.jpg'

img = cv2.imread(img_fullname)
img_out = img.copy()

[h, w, d] = img.shape
for i in range(d):
    img_out[:, :, i] = triangle(img[:, :, i].copy())
    
cv2.imwrite('assets/lotus-triangled.jpg', img_out)
```

## Output
This is a sample image:  
![groningen.jpg](https://raw.githubusercontent.com/Mamdasn/imTriangle/main/assets/groningen.jpg "groningen.jpg")  
The sample image after tirangle pixelation effect:  
![groningen-triangled.jpg](https://raw.githubusercontent.com/Mamdasn/imTriangle/main/assets/groningen-triangled.jpg "groningen-triangled.jpg")  
