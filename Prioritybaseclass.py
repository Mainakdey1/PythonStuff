class Priorityqueuebase:
    class _Item:
        
        __slots__='_key','_value'
        
        def __init__(self,k,v):
            self._key=k
            self._value=v
            
        def __it__(self,other):
            return self._key<other._key
        def _isempty(self):
            return len(self)==0
        
            