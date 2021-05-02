import numpy as np
import cv2
from imTriangle import triangle

cap = cv2.VideoCapture('assets/production ID_0000000.mp4')

# video without sound
video_out_name = 'assets/production ID_0000000-traingled.mp4'

i = 0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    print("\r", 100*i//length, "%", end='')
    
    h, w, d = frame.shape
    frame_eq = frame.copy()
    for dd in range(d): 
        frame_eq[:, :, dd] = triangle(frame[:, :, dd])

    fps = cap.get(cv2.CAP_PROP_FPS)
    if i==0:
        h, w, d = frame_eq.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_out = cv2.VideoWriter(video_out_name, fourcc, fps, (w, h))
    video_out.write(frame_eq)

    i+=1
cv2.destroyAllWindows()
video_out.release()
