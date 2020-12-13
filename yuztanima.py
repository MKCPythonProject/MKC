import cv2
import numpy as np
import Kisiler as kisi
from datetime import datetime
from datetime import date
import time
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('ogrenme/ogrenme.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    kontrol=False
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(150,0,0),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if id!=None:
            kisi_ad_soyad=kisi.Kisi.kisi_ad_getir(id)
            cv2.putText(im, kisi_ad_soyad, (x + 5, y + h - 5), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)
            kontrol=True
            time.sleep(3)#kişiyi tanıyınca 3 saniye bekle çık
            break


    cv2.imshow('KAPI GİRİŞ',im);

    if(cv2.waitKey(1)==ord('q') or kontrol==True):
        if kontrol==True: time.sleep(3)
        break
cam.release()

cv2.destroyAllWindows()
