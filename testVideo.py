import os.path
import numpy as np
import matplotlib.pyplot as plt

import cv2
import timeit


'''
# reference 
Frame per sec : https://deep-eye.tistory.com/15
Functions in openCv : https://3001ssw.tistory.com/166

Recognize face : https://m.blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221129242278&proxyReferer=https:%2F%2Fwww.google.com%2F
pixel : https://076923.github.io/posts/Python-opencv-34/

'''

# load video file 
vidAdd = os.path.abspath("sample.mp4")
cap = cv2.VideoCapture(vidAdd)

#B27.mp4
#Serum.mp4
#AIM.mp4
#B27_2.mp4
#B27_3.mp4

if cap.isOpened() == False:
    print("Wrong directory. Check address again!")
    exit()
    

'''
#재생할 파일의 넓이 얻기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#재생할 파일의 높이 얻기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#재생할 파일의 프레임 레이트 얻기
fps = cap.get(cv2.CAP_PROP_FPS)    
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#저장할 파일 이름
filename = 'grayRose.avi'

#파일 stream 생성
out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))    
'''

delta = []

i = 0 # - 
while True:
    ret, frame = cap.read()
    
    if frame is None:
    #if i == 10:
        break
    
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    #print(frame)
    #print(grayFrame)
    
    
    
    if i > 0:
        delta.append( np.sum((grayFrame - oldGrayFrame)**2) )
    
        
        
    oldGrayFrame = grayFrame 
    i += 1    


#with plt.style.context(['science','ieee']): 
with plt.style.context(['science', 'muted']):        
    #colors = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    colors = np.array(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
    fig1, ax1 = plt.subplots()
    fig1.set_figwidth(5)
            
        
    xPlot = np.linspace(2, i, i-1)    
    plt.plot(xPlot, delta)    
    
    '''
    fps 
    
    while True:
        ret, frame = video.read()
    
        if ret is True: 
    
            cv2.imshow('video', frame)
    
            if cv2.waitKey(1) > 0:
                break
    '''