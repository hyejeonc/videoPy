import os.path
import numpy as np
import math
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
vidArray = ['Serum', 'AIM', 'B27']

distArray = []
xPlotArray = []
fpsArray = []


for vid in vidArray:    
    # load video file 
    vidPath = os.path.abspath("vid/" + vid + ".mp4")
    vidObj = cv2.VideoCapture(vidPath)
    
    fps = vidObj.get(cv2.CAP_PROP_FPS)
    fpsArray.append(fps)
    #B27.mp4
    #Serum.mp4
    #AIM.mp4
    #B27_2.mp4
    #B27_3.mp4
    
    if vidObj.isOpened() == False:
        print("Wrong directory. Check address again!")
   
        
    
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
    
    dist = []
    
    i = 0
    while True:
        ret, frame = vidObj.read()
        
        if frame is None:
        #if i == 10:
            distArray.append(dist)
            xPlotArray.append(i)
            break
        
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        
        #print(frame)
        #print(grayFrame)
        
        
        
        if i > 0:
            #frameDiff = (grayFrame - oldGrayFrame)**2
            #dist.append(np.sum(np.sqrt(frameDiff)))
            dist.append(np.sum(np.absolute(grayFrame - oldGrayFrame)))
            
            '''
            frameDist = np.sqrt(frameDiff)
            
            m, n = np.shape(frameDist)
            
            sum = 0
            for i in range(m):
                for j in range(n):
                    sum += frameDist[i,j]
            
            print(sum)
            dist.append( sum )  # frame 의 가로 세로 크기가 같아야 비교 가능! 
            '''

        oldGrayFrame = grayFrame 
        i += 1    
    

#with plt.style.context(['science','ieee']): 
with plt.style.context(['science', 'muted']):  
    #colors = ['blue', 'orange', 'green', 'red', 'purple']      
    #colors = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    #colors = np.array(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
    lines = ['-', '--', '-.', ':']

            
        
    #xPlot = np.linspace(2, i, i-1)    
    
    for i in range(len(vidArray)):
    #    print(i)
        fig, ax = plt.subplots()
        fig.set_figwidth(5)
        
        ax.plot(np.linspace(0, xPlotArray[i],xPlotArray[i]-1 ), distArray[i], label=str(vidArray[i]))    
    
        ax.autoscale(tight=True)
        
        #fig.suptitle("Reduced position of bubbles ", fontsize=12, x=0.55, y=1.005)
        #ax.set_title(r'$\Delta P $ = 30, $\xi_L(0) = 0.050$, $\xi_R(0) = 0.055$, $\tau = 10^{-5}$', fontsize=8)
        
        fig.tight_layout() 
        
        ax.set_xlim(0.0, 630)
        #ax.set_ylim(0.0, 1.0)
        ax.set_ylabel(r"$\delta$")
        ax.set_xlabel(r"Frame")
        ax.set_yscale('log')
        ax.legend()
        fig.show()
        #fig.savefig('fig/.pdf')
        fig.savefig('fig/test-' + str(vidArray[i]) '.jpg', dpi=500)
    
    
    
    
    
    
    
    
    '''
    fps 
    
    while True:
        ret, frame = video.read()
    
        if ret is True: 
    
            cv2.imshow('video', frame)
    
            if cv2.waitKey(1) > 0:
                break
    '''