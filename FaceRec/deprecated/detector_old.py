import cv2
import numpy as np
import sqlite3
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("recognizer/trainingData.yml")
faceDetect = cv2.CascadeClassifier('/Users/josephawwal/Downloads/FaceRec/Classifiers/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture()

path = 'dataSet'

def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID="+str(id)
    cursor = conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

id=0
#font = cv2.FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1

bottomLeftCornerOfText = (255,255)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 1
fontColor = (255,255,255)
lineType = 2

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2 )
        profile = getProfile(id)
        if(conf<50):
            if(profile != None):
                cv2.putText(img,
                            str(profile[0]),
                            (x, y + h + 5),
                            font,
                            fontScale,
                            fontColor,
                            lineType
                            ),
                cv2.putText(img,
                            str(profile[1]),
                            (x,y+h+30),
                            font,
                            fontScale,
                            fontColor,
                            lineType
                ),
                cv2.putText(img,
                            str(profile[2]),
                            (x, y + h + 60),
                            font,
                            fontScale,
                            fontColor,
                            lineType
                            ),
                cv2.putText(img,
                            str(profile[3]),
                            (x, y + h + 90),
                            font,
                            fontScale,
                            fontColor,
                            lineType
                            ),




        else:
            cv2.putText(img,
                        'Unknown',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType
                        )


    cv2.imshow("Face", img)
    if(cv2.waitKey(1)==ord('q')):
        break

cam.release()
cv2.destroyAllWindows()