class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a scalar

    def __mul__(self,other):
        #If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self,other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self,other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self
    
    def __sub__(a,b):
         "Returns a vector which is the difference of a and b."
         return a+(-b)

    __eq__ = equal

    def __str__(v):
        "pretty-printing"
        try:
            D_list = sorted(v.D)
        except TypeError:
            D_list = sorted(v.D, key=hash)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(v[k], int) or isinstance(v[k], float) else (k,(1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        s1 = ''.join(['{0:>{1}}'.format(k,wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k],wd[k],numdec) if isinstance(v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        return Vec(self.D, self.f.copy())


def getitem(v,d):
    "Returns the value of entry d in v"
    assert d in v.D
    if d in v.f:
        return v.f[d]
    else:
        return 0
def setitem(v,d,val):
    "Set the element of v with label d to be val"
    assert d in v.D
    v.f[d] = val

def equal(u,v):
    "Returns true iff u is equal to v"
    assert u.D == v.D
    #if len(u.f) != len(v.f):
    #    print('domain is even not equal')
    #    return False
    for i in u.f:
        if i in v.f:
            if v.f[i] != u.f[i]:
                #print('same domain, not same codomain')
                return False
        else:
            if u.f[i] != 0:
                #print('the fommer , not 0')
                return False
    for i in v.f:
        if i not in u.f:
            if v.f[i] != 0:
                #print('the latter,not 0')
                return False
    return True
def add(u,v):
    "Returns the sum of the two vectors"
    assert u.D == v.D
    c = Vec(u.D,{})
    for i in v.f:
        if i not in u.f:
            c.f[i] = v.f[i]
        else:
            c.f[i] = v.f[i] + u.f[i]
    return c

def dot(u,v):
    "Returns the dot product of the two vectors"
    assert u.D == v.D
    a = 0
    for i in u.f:
        if i in v.f:
            a = a + (u.f[i]*v.f[i])
    return a

def scalar_mul(v, alpha):
    "Returns the scalar-vector product alpha times v"
    a=Vec(v.D,{})
    for i in v.f:
        a.f[i] = alpha*v.f[i]
    return a

def neg(v):
    "Returns the negation of a vector"
    a = Vec(v.D,{})
    for i in v.f:
        a.f[i] = v.f[i] * -1
    return a
