import cv2 as cv
import mediapipe as mp
# import controller as cnt
cap  = cv.VideoCapture(0)
mphand=mp.solutions.hands
hands = mphand.Hands(min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
fingercordinates = [(8,6),(12,10),(16,14),(20,18)]
thumbcordinates = [4,2]
while True:
    success,img=cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    multi =result.multi_hand_landmarks
    if multi:
        handPoins =[]
        for handsLMS in multi:
            mpDraw.draw_landmarks(img,handsLMS,mphand.HAND_CONNECTIONS)
            for idx,ln in enumerate(handsLMS.landmark):
                # print(idx,ln)
                h,w,c= img.shape
                cx,cy= int(w*ln.x) ,int(h*ln.y)
                handPoins.append((cx,cy))
            for points in handPoins:
                cv.circle(img, points,10,(255,0,0),cv.FILLED)
            count =0
            for coordinate in fingercordinates:
                if(handPoins[coordinate[0]][1]<handPoins[coordinate[1]][1]):
                    count+=1
            if handPoins[thumbcordinates[0]][0]>handPoins[thumbcordinates[1]][0]:
                count+=1
            # cv.putText(img,str(count),(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            print(count)
            if count == 5:
                cv.putText(img,"hai",(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            elif handPoins[fingercordinates[0][0]] > handPoins[fingercordinates[0][1]] and handPoins[fingercordinates[1][0]] > handPoins[fingercordinates[1][1]]:
                cv.putText(img,"peace",(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            elif count==0:
                cv.putText(img,"hello",(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            elif count ==3:
                cv.putText(img,"super",(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            elif count ==1 and handPoins[thumbcordinates[0]]>handPoins[thumbcordinates[1]]:
                cv.putText(img,"like",(100,150),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
            
            
                
            # cnt.led(count)
    # cv.imshow("Finger Counter",imgRGB)
    cv.imshow("count the fingers",img)
    cv.waitKey(10)
