
from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec


def rep2vec(u, veclist):
    '''
    Input:
        - u: a vector as an instance of your Vec class with domain set(range(len(veclist)))
        - veclist: a list of n vectors (as Vec instances)
    Output:
        vector v (as Vec instance) whose coordinate representation is u
    '''
    return coldict2mat(veclist) * u



def vec2rep(veclist, v):
    '''
    Input:
        - veclist: a list of vectors (as instances of your Vec class)
        - v: a vector (as Vec instance) with domain set(range(len(veclist)))
             with v in the span of set(veclist).
    Output:
        Vec instance u whose coordinate representation w.r.t. veclist is v
    '''
    return solve(coldict2mat(veclist),v)




def is_superfluous(L, i):
    '''
    Input:
        - L: list of vectors as instances of Vec class
        - i: integer in range(len(L))
    Output:
        True if the span of the vectors of L is the same
        as the span of the vectors of L, excluding L[i].

        False otherwise.
    '''
    a = L[:]
    a.remove(L[i])
    M = coldict2mat(a)
    result = solve(M,L[i])
    if ((L[i] - M * result) * (L[i] - M * result)) < 1e-14 :
        return True
    else:
        return False





def is_independent(L):
    '''
    input: a list L of vectors (using vec class)
    output: True if the vectors form a linearly independent list.
    '''
    for i in range(len(L)):
        if is_superfluous(L,i):
            return False
    return True



def exchange(S, A, z):
    '''
    Input:
        - S: a list of vectors, as instances of your Vec class
        - A: a list of vectors, each of which are in S, with len(A) < len(S)
        - z: an instance of Vec such that A+[z] is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} U S - {w})
    '''
    C = A[:]
    D = S[:]
    C.append(z)
    if not is_independent(C):
        return z
    D.append(z)
    for i in D:
        if i not in A and i != z:
            if is_superfluous(D,D.index(i)):
                D.remove(i)
                return i
    return z