# -*- coding: utf-8 -*-

import cv2,os
import numpy as np
from PIL import Image
class foto_ogrenme():
    def __init__(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
        faces,Ids = self.getImagesAndLabels('kisi_fotolar') 
        recognizer.train(faces, np.array(Ids))
        recognizer.save('ogrenme/ogrenme.yml') 
        
    def getImagesAndLabels(self,path): 
    
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
