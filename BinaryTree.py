#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:02:18 2022

@author: rik
"""
import Tree as tree
class BinaryTree(tree):
    
    def left(self,p):
        
        raise NotImplementedError('must be implemented by a subclass')
    def right(self,p):
        raise NotImplementedError('must be implemented by a subclass')
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            

                    
        