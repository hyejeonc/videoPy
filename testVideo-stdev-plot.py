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
Contour plots : https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html
'''
vidArray = ['Serum', 'AIM', 'B27']
#vidArray = ['B27']
#vidArray = ['AIM']

distArray = []
xPlotArray = []
fpsArray = []
stdevArray = []

n=630

for vid in vidArray:    
    # load video file 
    vidPath = os.path.abspath("vid2/" + vid + ".mp4")
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
    sqSum = np.zeros([784,1104], dtype=np.float32)
    avgSum = np.zeros([784,1104], dtype=np.float32)
    while True:
        ret, frame = vidObj.read()
        
        if i >= 631:
        #if i == 10:
            #distArray.append(dist)
            #xPlotArray.append(i)
            print("i is : ", i)
            break
        
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayFrame = grayFrame.astype('float64')
 
        #print(frame)
        #print(grayFrame)
        
        
        
        if i < 631 and i >= 1:
            #frameDiff = (grayFrame - oldGrayFrame)**2
            #dist.append(np.sum(np.sqrt(frameDiff)))
            #print(i)
            #print("[0,0]", grayFrame[0,0])
            #print("[0,0]**2", grayFrame[0,0]**2)
            #sqSum += grayFrame**2 #np.square(grayFrame)
            #avgSum += grayFrame
            #print("sq[0,0]", np.square(grayFrame)[0,0])
            #print("array**2", (grayFrame**2)[0,0])
            #dist.append(np.sum(np.absolute(grayFrame - oldGrayFrame)))
            sqSum += np.absolute(grayFrame - oldGrayFrame)**2
            avgSum += np.absolute(grayFrame - oldGrayFrame)
        
        
        oldGrayFrame = grayFrame 
        i += 1    
    
    stdev = np.sqrt( (sqSum / i) - (avgSum/i)**2 ) 
    
    #stdev = np.sqrt( (sqSum / i) - (avgSum/i)**2 )
    stdevArray.append(stdev)

#with plt.style.context(['science','ieee']): 
with plt.style.context(['science', 'muted']):  
    #colors = ['blue', 'orange', 'green', 'red', 'purple']      
    #colors = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    #colors = np.array(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
    lines = ['-', '--', '-.', ':']

            
    m, n = np.shape(stdev)    
    #xPlot = np.linspace(2, i, i-1)    
    xList = np.linspace(0,n,n)
    yList = np.linspace(0,m,m)
    X, Y = np.meshgrid(xList, yList)
    
    for i in range(len(vidArray)):
    #    print(i)
        fig, ax = plt.subplots()
        fig.set_figwidth(5)
        
        #bounds=np.linspace(-1,1,10)
        cp = ax.contourf(X,Y,np.flip(stdevArray[i],0), vmin=0.0, vmax=40.0 )
        fig.colorbar(cp)
        #ax.plot(np.linspace(0, xPlotArray[i],xPlotArray[i]-1 )/fpsArray[i], distArray[i], label=str(vidArray[i]),color='b')    
    
        ax.autoscale(tight=True)
        
        #fig.suptitle("Reduced position of bubbles ", fontsize=12, x=0.55, y=1.005)
        ax.set_title(r"$\sigma$, " + str(vidArray[i]), fontsize=10)
        
        fig.tight_layout() 
        
        #ax.set_xlim(0.0, 630/30)
        #ax.set_ylim(0.0, 1.5e8)
        ax.set_ylabel(r"$y$ [Pixel]")
        ax.set_xlabel(r"$x$ [Pixel]")
        #ax.set_yscale('log')
        ax.legend()
        fig.show()
        #fig.savefig('fig/.pdf')
        fig.savefig('fig/test-contour-' + str(vidArray[i]) + '.jpg', dpi=500)
        fig.savefig('fig/test-contour-' + str(vidArray[i]) + '.pdf')
    
    
    
    
    
    
    
    
    '''
    fps 
    
    while True:
        ret, frame = video.read()
    
        if ret is True: 
    
            cv2.imshow('video', frame)
    
            if cv2.waitKey(1) > 0:
                break
    '''