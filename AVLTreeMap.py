import TreeMap as TreeMap


class AVlTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__='_height'
        def __init__(self,element,parent=None,left=None,right=None):
            super().__init__(element,parent,left,right)
            self._height=0
            
        def left_height(self):
            return self._left._height if self._left is not None else 0
        def right_height(self):
            return self._right._height if self._right is not None else 0
        def _recompute_height(self,p):
            p._node._height=1+max(   p._node.left_height(),p._node.right_height())
        def _isbalanced(self,p):
            return abs(p._node.left_height()-p._node.right_height()<=1)
        def _tall_child(self,p,favorleft=False):
            if p._node.left_height()+(1 if favorleft else 0) > p.right_height() :
               return self.left(p)
          
            else   :
               return self.right(p)
           
        def _tall_grandchild(self,p):
            child=self._tall_child(p)
            alignment=(child==self.left(p))
            return self._tall_child(child,alignment)
        def _rebalance(self,p):
            while p is not None:
                old_height=p._node._height
                if not self._isbalanced(p):
                    p=self._restructure(self._tall_grandchild(p))
                    self._recompute_height(self.left(p))
                    self._recompute_height(self.right(p))
                    
                self._recompute_height(p)
                if p._node._height==old_height:
                    p=None
                else:
                    self.parent(p)
                    
        def _rebalance_insert(self,p):
            self._rebalance(p)
            
        def _rebalance_delete(self,p):
            self._rebalance(p)
            
            
            
            
                    
                    
                    
        
            