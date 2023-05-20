# отличаются на глубину

def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
    pointerA, pointerB = a, b
        
    while pointerA != pointerB:
        pointerA = pointerA.parent if pointerA else b
        pointerB = pointerB.parent if pointerA else a
            
    return pointerA


def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
    ancestors = set()
    
    while a is not None:
        ancestors.add(a)
        a = a.parent
        
    while b is not None:
        if b in ancestors:
            return b
        b = b.parent