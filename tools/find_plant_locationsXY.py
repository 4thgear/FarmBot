import cv2
import numpy as np
from matplotlib import pyplot as plt
import math



def notInList(newObject):
    for detectedObject in detectedObjects:
        if math.hypot(newObject[0]-detectedObject[0],newObject[1]-detectedObject[1]) < thresholdDist:
            return False
    return True

num = list(range(4))
for i in range(len(num)):
    imgloc = r"pics/templates/main/foamSheet0.jpg"
    img_rgb = cv2.imread(imgloc)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    imgloc2 = r"pics/templates/main/holeWide"+str(num[i])+".jpg"
    template = cv2.imread(imgloc2,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = .77
    loc = np.where( res >= threshold)
    detectedObjects = []
    thresholdDist = 100
    cellImage = []
    for pt in zip(*loc[::-1]):
        if len(detectedObjects) == 0 or notInList(pt):
            detectedObjects.append(pt)
            cellImage.append(img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w])
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
            cv2.rectangle(img_rgb, (pt[0]+w//2 - 5,pt[1]+h//2 - 5), (pt[0]+w//2 + 5,pt[1]+h//2 + 5), (255,255,255), -1)
            cv2.circle(img_rgb,(pt[0]+w//2,pt[1]+h//2),20,(255,255,255),-1)
            #print(pt[0]+w/2,pt[1]+h/2)
##    cv2.namedWindow("hole "+str(num[i]),cv2.WINDOW_NORMAL)
##    cv2.resizeWindow("hole "+str(num[i]),400,700)
##    cv2.imshow("hole "+str(num[i]),img_rgb)
##    cv2.waitKey(1000) & 0xFF
##    cv2.destroyWindow("hole "+str(num[i]))
    print(str(num[i])+" "+str(len(detectedObjects)))
##for i in range(len(cellImage)):
##    cellImage[i] = cv2.medianBlur(cellImage[i],5)
##    cv2.imshow(str(i),cellImage[i])
##    cv2.waitKey() & 0xFF
##cv2.destroyAllWindows()

