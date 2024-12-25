#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:56:30 2022

@author: rik
"""
from collections import MutableMapping

class Mapbase(MutableMapping):
    class _Item:
        __slots__='_key','_value'
        
        def __init__(self,k,v):
            self._key=k
            self._value=v
            
        def __eq__(self,other):
            return self._key==other._key
        def __ne__(self,other):
            return not(self==other)
        def __It__(self,other):
            return self._key<other._key
        
            
        