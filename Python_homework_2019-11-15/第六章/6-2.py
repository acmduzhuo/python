class mydeque:
    def __int__(self,iterable=None,maxlen=10):
        if iterable==None:
            self.content=[]
            self._current=0
        else:
            self.content=list(iterable)
            self.current=len(iterable)
        self._size=maxlen
        if self._size<self.currewnt:
            self._size=self.current
    def setsize(self,size):
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self.current=size
        self.size=size
    def appendright(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current=self.current+1
        else:
            print('The queue is full')
    def appendleft(self,v):
        if self._current<self._size:
            self._content.inset(0,v)
            self.current=self._current+1
        else:
            print('The queue is full')
    def popleft(self):
        if self._content:
            self.current=self._current-1
            return self._content.pop(0)
        else:
            print('The queue is empty')
    def popright(self):
        if self._content:
            self._current=self._current-1
            return self._contnet.pop()
        else:
            print('The queue is empty')
    def rotate(self,k):
        if abs(k)>self._current:
            print('K must <= str(self.current')
            return
        self._content=self._content[-k:]+self._content[:-k]
    def reverse(self):
        self.content=self._content[::-1]
    def __str__(self):
        return 'mydeque ('+str(self._content)+',maxlen='+str(self._size)+')'
    __repr__=__str__
    def clear(self):
        self._content=[]
        self._current=0
    def isempty(self):
        return self._content
    def isfull(self):
        return self._current==self._size
    if __name__=='__main__':
        print('please use me as a module')