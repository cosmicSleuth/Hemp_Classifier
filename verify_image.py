import os

from PIL import Image


def VerifyImage(imageFolderPath):
    listImages = os.listdir(imageFolderPath)

    for img in listImages:
        print("checking: " + os.path.join(imageFolderPath, img))
        
        imgPath = os.path.join(imageFolderPath, img)
                
        try:
            img = Image.open(imgPath)
            exif_data = img._getexif()
        except ValueError as err:
            print(err)
            print("Error on image: ", os.path.join(imageFolderPath, img))
            
            
            
VerifyImage('dataset/plants/common')
VerifyImage('dataset/plants/hemp')
            