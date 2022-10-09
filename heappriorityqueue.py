#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:15:53 2022

@author: rik
"""
class Priorityqueuebase:
    class _Item:
        
        __slots__='_key','_value' #dnote:for some reason it is not possible to import this
        #module as a normal module
        
        def __init__(self,k,v):
            self._key=k
            self._value=v
            
        def __It__(self,other):
            return self._key<other._key
        
        def _isempty(self):
            return len(self)==0
        


class heappriorityqueue(Priorityqueuebase):
    
    def _parent(self,j):
        return (j-1)//2
    def _left(self,j):
        return 2*j+1
    def _right(self,j):
        return 2*j+2
    
    def _has_left(self,j):
        return self._left(j)<len(self._data)
    def _has_right(self,j):
        return self._right(j)<len(self._data)
    
    def _swap(self,i,j):
        
        self._data[i],self._data[j]=self._data[j],self._data[i]
        
    def _upheap(self,j):
        parent=self._parent(j)
        if j>0 and self._data[j]<self._data[parent]:
            self._swap(parent,j)
            self._upheap(parent)
            
    def _downheap(self,j):
        if self._has_left(j):
            left=self._left(j)
            smallchild=left
            if self._has_right(j):
                right=self._right(j)
                if self._data[right]<self._data[left]:
                    smallchild=right
            if self._data[smallchild]<self._data[j]:
                self._swap(smallchild,j)
                self._downheap(smallchild)
                
        
    #public behavior including constructor
    
    def __init__(self):
        self._data=[]
        
    def __len__(self):
        return len(self._data)
    
    def add(self,key,value):
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data)-1)

    def minimum(self):
        if self._isempty():
            raise ValueError('priority queue is empty')
        item=self._data[0]
        return item._key, item._value
    def remove_min(self):
        if self._isempty():
            raise ValueError('priority queue is empty')
        self._swap(0,len(self._data)-1)
        item=self._data.pop()
        self._downheap(0)
        return item._key,item._value
    
test=heappriorityqueue()

test.add(0,'a')
test.add(1,'b')
test.add(2,'c')

test.minimum()


    
    
            
        
