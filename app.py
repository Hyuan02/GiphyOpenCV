from threading import Thread
import numpy as np
import cv2
from enum import Enum

class StateProgram(Enum):
    play = 1
    pause = 2


class ImgThread(Thread):
    def __init__(self, listOfImages):
        Thread.__init__(self)
        self._images = listOfImages
        self._initialPosition = listOfImages.returnPointer()
        self._aux = self._initialPosition
        global globalStateApp
        globalStateApp = StateProgram.play

    def exhibit_image(self):
        if self._aux is None:
            self._aux = self._initialPosition
        cv2.imshow('Gif exhibition', self._aux.elem.img)

        self.wait_for_key()
        self._aux = self._aux.next
        pass


    def wait_for_key(self):
        global globalStateApp
        output = cv2.waitKey(self._aux.elem.delay)
        if output != -1:
            print(output)
        if output == 101:
            print('Pausando programa!')
            globalStateApp = StateProgram.pause
            self.new_console()
        elif output == 113:
            print('Saindo de programa!')
            cv2.destroyAllWindows()
            exit(0)


    def new_console(self):
        global globalStateApp
        print('Nesse gif existem ' + self._images.length().__str__() + ' fotos.')
        out = input('Digite o número de qual foto você deseja editar o tempo: ')
        result = int(out)
        duration = input('Digite a duração de quantos milisegundos terá o novo tempo: ')
        if self.editImageDuration(result, duration):
            input('Duração alterada. Pressione enter para voltar.')
            globalStateApp = StateProgram.play
        else:
            input('Erro. Pressione enter para voltar.')
            globalStateApp = StateProgram.play
        pass

    def editImageDuration(self, result, duration):
        output = None
        output = self._images.get(result)
        if output is not None:
            if duration.isnumeric():
                newDuration = int(duration)
                output.elem.delay = newDuration
                return True
        return False

    def run (self):
        print('pressione E para Editar a sequencia de imagens ou Q para sair')
        while True:
            if globalStateApp == StateProgram.play:
                self.exhibit_image()

