import cv2
import numpy as np

holeNum = [0,1,2,3]
for j in range(len(holeNum)):
    imgloc = r"pics/templates/single/hole"+str(holeNum[j])+".jpg"
    img = cv2.imread(imgloc,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cv2.imwrite('detected circles.jpg',cimg)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imwrite('pics/results/circles/hole'+str(holeNum[j])+'Detected.jpg',cimg)


