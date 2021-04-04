import numpy as np
import cv2
from data_structure import LinkedImageList, Node, ImgType
import glob
from app import ImgThread

def getNextImage(aux, initialPosition):
    if aux is None:
        aux = initialPosition
    cv2.imshow('Gif exhibition', aux.elem.img)
    wait_for_key_in_delay(aux.elem.delay)
    aux = aux.next
    return aux

def wait_for_key_in_delay(delay):
    keyToKnow = cv2.waitKeyEx(delay)

if __name__ == '__main__':
    listOfImages = LinkedImageList()
    filesInFolder = glob.glob("assets/*")


    for imagePath in filesInFolder:
        listOfImages.insert(ImgType(cv2.imread(imagePath, cv2.IMREAD_COLOR), 100))

    imgThread = ImgThread(listOfImages)
    imgThread.start()


    pass

