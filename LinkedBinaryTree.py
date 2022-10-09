#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:18:16 2022

@author: rik
"""
import BinaryTree as BinaryTree
class LinkedBinaryTree(BinaryTree):
    
    class _Node():
        __slots__='_element','_parent','_right','_left'
        def __init__(self,element,parent,right,left):
            self._element=element
            self._parent=parent
            self._right=right
            self._left=left
    class Position(BinaryTree.Position):
        
        def __init__(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def _validate(self,p):
            if not isinstance(p,self.Position):
                raise TypeError(' p must be proper position type')
            if p._container is not self:
                raise ValueError(' p does not belong to this container')
            if p._node._parent is p._node:
                raise ValueError('p is deprecated')
            return p._node
            
        def _make_position(self,node):
            
            return self.Position(self,node) if node is not None else None
        
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
        return self._make_position(self.root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node=self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        node=self._validate(p)
        count=0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
            
        return count
    
    def _add_root(self,e):
        if self._root is not None: raise ValueError('root already exists')
        self._size=1
        self._root=self._Node(e)
        return self._make_position(self._root)
    def _add_left(self,e):
        node=self._validate(e)
        if node._left is not None: raise ValueError('left child already exists')
        self._size+=1
        node._left=self._Node(e,node)
        return self._make_position(node._left)
    
    def _add_right(self,e):
        node=self._validate(e)
        if node._right is not None: raise ValueError('right child already exists')
        self._size+=1
        node._right=self._Node(e,node)
        return self._make_position(node._right)
    
        
        
    def _replace(self,p,e):
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        node=self._validate(p)
        if self.num_children(p)==2: raise ValueError('p has two children')
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1 
        node._parent=node
        return node._element
    def _attach(self, p, t1,t2):

        node=self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('all trees must be concordant types')
        self._size+=len(t1)+len(t2)
        if not t1.is_empty():
            t1._root._parent=node
            node._left=t1._root
            t1._root=None
            t1._size=0
        if not t2.is_empty():
            t2._root._parent=node
            node._left=t1._root
            t2._root=None
            t2._size=0
            
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
