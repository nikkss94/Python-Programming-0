def setify(a):
    b = []
    for x in a:
        if x not in b:
            b += [x]
    return b
        
    return new_a


def diff(a, b):
    m = []
    for x in a:
        if x not in b:
            m += [x]
    return m


def union(a, b):
    m = []
    for x in a:
        m += [x]
    for y in b:
        if y not in m:
            m += [y]
    return m
        
            
def intersection(a, b):
    m = []
    for x in a:
        for y in b:
            if x == y:
                m += [x]
    return m


def cartesian_product(a, b):
    m = []
   
    for x in a:
        for y in b:
            m_1+ = (x,y)
            
    return m


