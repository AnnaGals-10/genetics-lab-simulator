class MinHeap:

    def __init__(self, items=[]):
        self.__heapify(items)

    def inserir(self, x):
        (self.__lst).append(x)
        self.__surar(len(self.__lst)-1)

    def obtenir_min(self):
        assert not self.buit()
        primer = self.__lst[1]
        darrer = (self.__lst).pop()
        if len(self.__lst) > 1:
            self.__lst[1] = darrer
            self.__enfonsar(1)
        return primer
    
    def buit(self):
        return self.__lst == [None]
    
    def __heapify(self,ll=[]):
        self.__lst = [None]
        for e in ll:
            self.__lst.append(ll)
        darrer_index = len(self.__lst)-1
        for i in range(darrer_index//2, 0, -1):
            self.__enfonsar(i)
 
    def __surar(self,i):
        if i>1 and self.__lst[i//2] > self.__lst[i]:
            self.__lst[i],self.__lst[i//2] = self.__lst[i//2],self.__lst[i]
            self.__surar(i//2)
 
    def __enfonsar(self,i):
        self.__n = len(self.__lst)-1
        self.__c = 2*i
        if self.__c <= n:
            if self.__c+1 <= self.__n and self.__lst[self.__c+1] < self.__lst[self.__c]:
                self.__c=self.__c+1
            if (self.__lst[i] > self.__lst[self.__c]):
                self.__lst[i],self.__lst[self.__c]=self.__lst[self.__c],self.__lst[i]
                self.__enfonsar(self.__c)

l = MinHeap([12,123,4,3,234,23,3,2])
