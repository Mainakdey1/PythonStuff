class _Doublelinkedlist:
    class _node:
        __slots__='_element','_nxt','_prev'
        def __init__(self,element,nxt,prev):
            self._element=element
            self._prev=prev
            self._nxt=nxt
    def __init__(self):
        self._header=self._node(None,None,None)
        self._trailer=self._node(None,None,None)
        self._header._nxt=self._trailer
        self._trailer._prev=self._header
        self._size=0
        
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def _ins_between(self,e,pred,succ):
        newest=self._node(e,pred,succ)
        pred._nxt=newest
        succ._prev=newest
        self._size+=1
        return newest
    def _delete_node(self,node):
        predecessor=node._prev
        successor=node._nxt
        predecessor._nxt=successor
        successor._prev=predecessor
        self._size-=1
        element=node._element
        node._prev=node._nxt=node._element=None
        return element
    
class ldeq(_Doublelinkedlist):
    def first(self):
        if self.is_empty():
            raise ValueError('deque is empty')
        return self._header._nxt._element
    def last(self):
        if self.is_empty():
            raise ValueError('deque is empty')
        return self._trailer._prev._element
    def ins_first(self,e):
        self._ins_between(e,self._header,self._header._nxt)   
    def ins_last(self,e):
        self._ins_between(e,self._trailer._prev,self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise  ValueError('cannot delete from an empty deque')
        return self._delete_node(self._header._nxt) 
    def delete_last(self):
        if self.is_empty():
            raise Exception('cannot delete from an empty deque')
        return self._delete_node(self._trailer._prev)
    
    
    
        