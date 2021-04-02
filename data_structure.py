from abc import ABC, abstractmethod

class List(ABC):
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

class Node():
    def __init__(self, elem):
        self.next = None
        self.elem = elem


class LinkedImageList(List):
    def __init__(self):
        self._header = None
        self._tail = None
    def insert(self, elem):
        if self._header is None:
            self._header = Node(elem)
            self._tail = self._header
        else:
            currentTail = self._tail
            self._tail = Node(elem)
            currentTail.next = self._tail
    def remove(self, elem):
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

    def count(self, elem):
        if self._header is not None:
            aux = self._header
            occurrences = 0
            while aux is not None:
                if aux.elem == elem:
                    occurrences+=1
                aux = aux.next
            return occurrences
        return 0

    def clear(self):
        self._header = None
        self._tail = None


    def index(self, elem):
        if self._header is not None:
            aux = self._header
            occurrence = 0
            while aux is not None:
                if aux.elem == elem:
                    return occurrence
                aux = aux.next
                occurrence+=1
        return -1
    def returnPointer(self):
        aux = self._header
        return aux



class ImgType:
    def __init__(self, img, delay):
        self.img = img
        self.delay = delay