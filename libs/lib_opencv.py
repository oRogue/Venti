import cv2 as cv
import numpy as np
import urllib.request
import random

### OpenCV Utils ###

# Resize
def rescaleFrame(frame,scale=0.75):    # Takes a frame a resize it to the scale value
    # Works with Image , Video , Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# Convert img to grayscale
def grayScale(img):
    grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return(grayImg)

### OpenCV Main ###

# Reading Images
def readImage():
    img = cv.imread('assets/venti_face_test.jpg')  #bind image to img
    resized_img = rescaleFrame(img,0.3) # calls resize function | Change scale on 2nd parameter
    return resized_img

# Face Detection - Haarcascade(Human)
def faceDetection(url):
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    
    url_response = urllib.request.urlopen(req)
    img = cv.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)
    gray_img = grayScale(img)
    face_cascade = cv.CascadeClassifier("openCV\haarcascades\haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 2) # detects faces in the input image
    
    # use this to redo with a different haarcascade if no faces dectected
    # numFaces = len(faces) # amount of faces
    
    for (x,y,w,h) in faces: # loop over all the detected faces
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        # Use random to generate random text
        textArr = ["test", "test2", "test3"]
        cv.putText(img, random.choice(textArr), (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,255), 2,)
        
    # resized_img = rescaleFrame(img,0.3)
    final_img = cv.imencode('.jpg', img)[1].tobytes()
    return(final_img)

