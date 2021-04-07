import numpy as np
import cv2
from data_structure import LinkedList, ImgType
import glob
from app import ImgThread


if __name__ == '__main__':
    listOfImages = LinkedList() #instancia estrutura de lista encadeada.
    filesInFolder = glob.glob("assets/*") #lê arquivos de pasta.


    for imagePath in filesInFolder:
        listOfImages.insert(ImgType(cv2.imread(imagePath, cv2.IMREAD_COLOR), 100))

    imgThread = ImgThread(listOfImages) #instancia thread de exibição de imagens
    imgThread.start() #inicia thread.


