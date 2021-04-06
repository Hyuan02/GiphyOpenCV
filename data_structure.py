from abc import ABC, abstractmethod


class List(ABC):
    """
    Classe abstrata contendo funções comuns da implementação de uma lista.
    """
    @abstractmethod
    def insert(self, elem):
        pass
    @abstractmethod
    def remove(self, elem):
        pass
    @abstractmethod
    def count(self, elem):
        pass
    @abstractmethod
    def clear(self):
        pass
    @abstractmethod
    def index(self, elem):
        pass


class Node:
    """
    Classe representando um nó armazenador de elementos em uma lista.
    """
    def __init__(self, elem):
        self.next = None
        self.elem = elem


class LinkedList(List):
    """
    Implementação de uma lista, na estrutura de lista encadeada.
    """

    def __init__(self):
        """
        Construtor da lista.
        """
        self._header = None
        self._tail = None

    def insert(self, elem):
        """
        Inserção de um elemento na última posição da lista.
        :param elem: Elemento a ser inserido.
        :return: None
        """
        if self._header is None:
            self._header = Node(elem)
            self._tail = self._header
        else:
            currentTail = self._tail
            self._tail = Node(elem)
            currentTail.next = self._tail

        pass

    def remove(self, elem):
        """
        Remoção da primeira ocorrência de um elemento na lista.
        :param elem: Elemento a ser removido.
        :return: None
        """
        if self._header is not None:
            if self._header.elem == elem:
                self._header = self._header.next
            else:
                aux = self._header.next
                prev = self._header
                while aux is not None:
                    if aux.elem == elem:
                        prev.next = aux.next
                        if self._tail == aux:
                            self._tail = prev
                        break
                    prev = aux
                    aux = aux.next
        pass


    def count(self, elem) -> int:
        """
        Contagem das ocorrências de um elemento.
        :param elem: Elemento a ser contado.
        :return: int - número de ocorrências.
        """
        if self._header is not None:
            aux = self._header
            occurrences = 0
            while aux is not None:
                if aux.elem == elem:
                    occurrences += 1
                aux = aux.next
            return occurrences
        return 0

    def clear(self):
        """
        Limpeza da lista.
        :return: None
        """
        self._header = None
        self._tail = None
        pass

    def index(self, elem) -> int:
        """
        Índice da primeira ocorrência de um elemento
        :param elem: Elemento a ser buscado.
        :return: int - Índice do elemento.
        """
        if self._header is not None:
            aux = self._header
            occurrence = 0
            while aux is not None:
                if aux.elem == elem:
                    return occurrence
                aux = aux.next
                occurrence += 1
        return -1

    def return_pointer(self) -> Node:
        """
        Retorna um ponteiro auxiliar apontando para o cabeçalho da lista.
        :return: Node - Ponteiro Auxiliar
        """
        aux = self._header
        return aux

    def length(self) -> int:
        """
        Retorna o tamanho da lista
        :return: int - Contendo o tamanho da lista.
        """
        occurrence = 0
        if self._header is not None:
            aux = self._header
            while aux is not None:
                occurrence += 1
                aux = aux.next
        return occurrence


    def get(self, index) -> Node:
        """
        Retorna um elemento em um determinado índice.
        :param index: Índice a ser procurado.
        :return: Node|None - Elemento no índice, caso exista
        """
        occurrence = 0
        if self._header is not None:
            aux = self._header
            while aux is not None and occurrence < index:
                occurrence+=1
                aux = aux.next
            if aux is None:
                raise IndexError
            return aux


class ImgType:
    """
    Classe usada para representar uma entidade imagem,
    que contém sua duração, e sua imagem instanciada do OpenCV.
    """
    def __init__(self, img, delay):
        self.img = img
        self.delay = delay
