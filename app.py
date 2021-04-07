from threading import Thread
import numpy as np
import cv2
from enum import Enum

class StateProgram(Enum):
    play = 1
    pause = 2


class ImgThread(Thread): #Herda de thread para poder rodar paralelamente.
    def __init__(self, listOfImages):
        """
        Inicia o processo de exibição de imagens, com a lista de imagens fornecida.
        :param listOfImages: Lista de imagens instanciada do opencv.
        """
        Thread.__init__(self)
        self._images = listOfImages
        self._initialPosition = listOfImages.return_pointer() # refêrencia para o cabeçalho da lista.
        self._aux = self._initialPosition # ponteiro móvel começa no início da lista.
        global globalStateApp # inicia a variável que controla o estado do programa
        globalStateApp = StateProgram.play

    def exhibit_image(self):
        """
        Exibe a próxima imagem contida na lista de imagens, ou caso tenha chegado ao final da lista,
        volta para o começo.

        :return:
        """
        if self._aux is None:
            self._aux = self._initialPosition
        cv2.imshow('Gif exhibition', self._aux.elem.img)

        self.wait_for_key() # espera por um pressionamento de tecla, no delay do gif
        self._aux = self._aux.next
        pass


    def wait_for_key(self):
        """
        Função que espera por um pressionamento de tecla no delay de quadros.
        :return:
        """
        global globalStateApp #pega referência de variável global de estado do app.
        output = cv2.waitKey(self._aux.elem.delay) #espera o pressionamento de uma tecla pelo delay do gif.
        if output != -1: #se for diferente de nenhuma loga o valor da tecla pressionada.
            print(output)
        if output == 101: #caso seja tecla E, pausa o programa.
            print('Pausando programa!')
            globalStateApp = StateProgram.pause
            self.new_console()
        elif output == 113: #caso seja tecla 'Q' sai do programa.
            print('Saindo de programa!')
            cv2.destroyAllWindows() #destrói as instâncias.
            exit(0)


    def new_console(self):
        """
        Inicia o programa de console, para mudança de tempos de quadros.
        :return:
        """

        global globalStateApp #pega referencia global do estado do app.
        print('Nesse gif existem ' + self._images.length().__str__() + ' fotos.')
        out = input('Digite o número de qual foto você deseja editar o tempo: ')
        if out.isnumeric():
            result = int(out) # converte entrada para inteiro
            duration = input('Digite a duração de quantos milisegundos terá o novo tempo: ')
            if self.editImageDuration(result, duration): #caso operação retorne sucesso
                input('Duração alterada. Pressione enter para voltar.')
                globalStateApp = StateProgram.play
                return
        input('Erro. Pressione enter para voltar.') #caso operação dê errado.
        globalStateApp = StateProgram.play #retorna estado para tocar animação.
        pass

    def editImageDuration(self, result, duration):
        """
        Função responsável por editar a duração de um determinado quadro em um gif
        :param result: quadro a ser editado.
        :param duration: nova duração.
        :return: true caso operação seja um sucesso, false caso ocorra algum erro.
        """
        try:
            output = None
            output = self._images.get(result) #pega imagem correspondente ao index desejado.
            if output is not None: #caso imagem exista
                if duration.isnumeric():
                    newDuration = int(duration) #converte duração para inteiro.
                    output.elem.delay = newDuration #atribui novo delay para animação.
                    return True
            return False
        except:
            print('Erro ao mudar imagem. Tente novamente.') #caso ocorra algum erro de ele nao encontrar a imagem.

    def run (self):
        """
        Função responsável por rodar a thread de exibição de imagens.
        :return:
        """
        print('pressione E para Editar a sequencia de imagens ou Q para sair')
        while True:
            if globalStateApp == StateProgram.play: #enquanto o estado global da aplicação for play
                self.exhibit_image() #exibe a próxima imagem.

