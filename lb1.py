import numpy as np 
from PIL import Image 
from random import * 
from math import * 
img_mat = np.zeros((200, 200,3), dtype = np.uint8) 
def drawline(img_mat, x0, y0, x1, y1, color): 
    count =100 
    step = 1.0/count 
    for t in np.arange (0,1, step): 
        x = round ((1.0 - t)*x0 + t*x1) 
        y = round ((1.0 - t)*y0 + t*y1) 
        img_mat[y, x] = color  
 
def drawline2(img_mat, x0, y0, x1, y1, color): 
    count = sqrt((x0 - x1)**2 + (y0 - y1)**2) 
    step = 1.0/count 
    for t in np.arange (0,1,step): 
        x = round ((1.0 - t)*x0 + t*x1) 
        y = round ((1.0 - t)*y0 + t*y1) 
        img_mat[y,x] = color   
  
 
def drawline3(img_mat, x0, y0, x1, y1, color): 
    for x in range (x0,x1): 
        t = (x-x0)/(x1-x0) 
        y = round((1.0-t)*y0+t*y1)  
        img_mat[y,x]= color 
 
def drawline4(img_mat, x0, y0, x1, y1, color): 
    if (x0>x1): 
        x0, x1 = x1, x0 
        y0, y1 = y1, y0 
    for x in range (x0,x1): 
        t = (x-x0)/(x1-x0) 
        y = round((1.0-t)*y0+t*y1)  
        img_mat[y,x]= color 
def drawline5(img_mat, x0, y0, x1, y1, color): 
    xchange = False 
    if (abs(x0-x1) < abs(y0-y1)): 
            x0,y0 = y0,x0  
            x1, y1 = y1,x1 
            xchange = True 
    if (x0>x1): 
        x0, x1 = x1, x0 
        y0, y1 = y1, y0 
    for x in range (x0,x1): 
        t = (x-x0)/(x1-x0) 
        y = round((1.0-t)*y0+t*y1) 
         
        if (xchange): 
            img_mat[x,y] = color  
        else: 
            img_mat[y,x]= color 
 
def drawline6(img_mat, x0, y0, x1, y1, color): 
   
    y = y0 
    dy = abs(y1 - y0)/(x1 - x0) 
    derror = 0.0 
    y_update = 1 if y1 >y0 else -1 
 
    for x in range (x0, x1): 
         
 
        img_mat[y, x] = color 
 
        derror += dy 
        if (derror > 0.5): 
            derror -= 1.0 
            y += y_update 
def drawline7(img_mat, x0, y0, x1, y1, color): 
    xchange = False 
    if (x0>x1): 
        x0, x1 = x1, x0 
        y0, y1 = y1, y0 
    y = y0 
    dy = abs(y1 - y0)/(x1 - x0) 
    derror = 0.0 
    y_update = 1 if y1 >y0 else -1 
 
    for x in range (x0, x1): 
         
 
        img_mat[y, x] = color 
 
        derror += dy 
        if (derror > 0.5): 
            derror -= 1.0 
            y += y_update 
def drawline8(img_mat, x0, y0, x1, y1, color): 
    xchange = False
    if (abs(x0-x1) < abs(y0 - y1)):
        x0,y0 = y0,x0
        x1,y1 = y1,x1
        xchange = True
 
    if(x0>x1):
        x0,x1=x1,x0
        y0,y1=y1,y0
    y=y0
    dy=2*abs(y1-y0)
    derror = 0
    y_update = 1 if y1>y0 else -1

    for x in range(x0, x1):
        if (xchange):
            img_mat[x,y] = color
        else:
            img_mat[y,x] = color
        derror += dy
        if (derror > (x1-x0)):
            derror -= 2*(x1-x0)
            y += y_update



import numpy as np 
from PIL import Image, ImageOps 
from random import * 
from math import * 
def draw(img_mat, verticals, color): 
   for i in verticals: 
      x=round(i[0]*1000)+1000 
       
       
      y=round(i[1]*1000)+1000 
      img_mat[x,y] = color  

    
    
img_mat = np.zeros((2000, 2000,3), dtype = np.uint8) 
file = open('model_1.obj') 
vertices = []
poligons = []
for  s in file:
    s_list =  s.split()
    if(s_list[0]=='v'):
        vertices.append([float(s_list[1]), float(s_list[2]), float(s_list[3])])
    if(s_list[0]=='f'):
        poligons.append([int(s_list[1].split('/')[0]), int(s_list[2].split('/')[0]), int(s_list[3].split('/')[0])])
 
for i in range (2000): 
    for j in range(2000): 
        img_mat[i,j,0] = 0 

for k in range(len(poligons)):
    x0 = vertices[poligons[k][0]-1][0] * 10000 + 1000
    y0 = vertices[poligons[k][0]-1][1] * 10000 + 500
    x1 = vertices[poligons[k][1]-1][0] * 10000 + 1000
    y1 = vertices[poligons[k][1]-1][1] * 10000 + 500
    x2 = vertices[poligons[k][2]-1][0] * 10000 + 1000
    y2 = vertices[poligons[k][2]-1][1] * 10000 + 500
    drawline8(img_mat,int(x0),int(y0),int(x1),int(y1),255)
    drawline8(img_mat,int(x1),int(y1),int(x2),int(y2),255)
    drawline8(img_mat,int(x0),int(y0),int(x2),int(y2),255)
 
 
 

img = Image.fromarray(img_mat,mode='RGB')
img= ImageOps.flip(img )
img.save('img.png')
