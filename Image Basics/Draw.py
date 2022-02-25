# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
def CreateRectangle(event,x,y,flags,param):
    global img,ix,iy
    drawing=False
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix=x
        iy=y
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),thickness=-1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),thickness=-1)

    elif event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),thickness=-1)
        drawing=False



# %%
def main():
    global img,ix,iy
    ix=-1
    iy=-1
    img=np.zeros((512,512,3))
    cv2.namedWindow(winname='hello_world')
    cv2.setMouseCallback('hello_world',CreateRectangle)
    while True:
        cv2.imshow('hello_world',img)
        if cv2.waitKey(40)&0xFF==ord('q'):
            break
    cv2.destroyAllWindows()

# %%
main()



# %%
