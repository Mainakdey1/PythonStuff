
import numpy as np
import imageio.v3
import time
import sys
start_time=time.time()

sys.set_int_max_str_digits(10000000)

imgcolor=imageio.v3.imread(r"C:\Users\chestor\Desktop\galaxy.jpg")
rows, cols, rgb=imgcolor.shape

R=[]
G=[]
B=[]
for i in range(rows):
    for j in range(cols):
        B.append(imgcolor[i,j,0])
        G.append(imgcolor[i,j,1])
        R.append(imgcolor[i,j,2])

print(B)
count=0
