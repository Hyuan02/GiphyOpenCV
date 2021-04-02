import numpy as np
import cv2
from data_structure import LinkedImageList, Node, ImgType
import glob

if __name__ == '__main__':
    listOfImages = LinkedImageList()
    filesInFolder = glob.glob("assets/*")


    for imagePath in filesInFolder:
        listOfImages.insert(ImgType(cv2.imread(imagePath, cv2.IMREAD_COLOR), 100))

    initialPosition = listOfImages.returnPointer()
    aux = initialPosition
    while True:
        aux = initialPosition
        while aux is not None:
            cv2.imshow('Gif exhibition', aux.elem.img)
            cv2.waitKey(aux.elem.delay)
            aux = aux.next
    pass

