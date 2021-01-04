# -*- coding: utf-8 -*-
import cv2,os
import numpy as np
from PIL import Image
class foto_ogrenme():
    def __init__(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces,Ids = self.resim_getir('kisi_fotolar')
        recognizer.train(faces, np.array(Ids))
        recognizer.save('ogrenme/ogrenme.yml')

        self.goz_detector = cv2.CascadeClassifier("haarcascade_eye.xml")
        gozler, g_Ids = self.goz_resim_getir('kisi_fotolar')
        recognizer.train(gozler, np.array(g_Ids))
        recognizer.save('ogrenme/goz_ogrenme.yml')


    def resim_getir(self,path):
    
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        faceSamples=[]
        Ids=[]
        
        for imagePath in imagePaths:
    
            if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
                continue
    
            pilImage=Image.open(imagePath).convert('L')
            imageNp=np.array(pilImage,'uint8')
            Id=int(os.path.split(imagePath)[-1].split(".")[0])
            faces=self.detector.detectMultiScale(imageNp)
            
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids

    def goz_resim_getir(self, path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        gozSamples = []
        g_Ids = []

        for imagePath in imagePaths:

            if (os.path.split(imagePath)[-1].split(".")[-1] != 'jpg'):
                continue

            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            Id = int(os.path.split(imagePath)[-1].split(".")[0])
            gozler = self.goz_detector.detectMultiScale(imageNp)

            for (x, y, w, h) in gozler:
                gozSamples.append(imageNp[y:y + h, x:x + w])
                g_Ids.append(Id)
        return gozSamples,g_Ids