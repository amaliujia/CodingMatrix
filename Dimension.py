from vecutil import list2vec
from solver import solve
from matutil import listlist2mat, coldict2mat,mat2coldict,mat2rowdict,coldict2mat,rowdict2mat,identity
from mat import Mat
from GF2 import one
from vec import Vec
from independence import rank

def morph(S, B):
    '''
    Input:
        - S: a list of distinct Vec instances
        - B: a list of linearly independent Vec instances
        - Span S == Span B
    Output: a list of pairs of vectors to inject and eject
    '''

    list_to_return = []
    T = S[:]
    for v_inject in B:
        inject_list = v_inject
        for v_remove in T:
            u = vec2rep(T + inject_list, v_remove)
            if u * u > 1e-14:
                T.remove(v_remove)
                list_to_return.append (v_inject,v_remove)
    return list_to_return



def my_is_independent(L): 
    '''
    input:  A list, L, of Vecs
    output: A boolean indicating if the list is linearly independent
    '''

    if len(L) > rank(L):
        return False
    return True



def subset_basis(T): 
    '''
    input: A list, T, of Vecs
    output: A list, S, containing Vecs from T, that is a basis for the
    space spanned by T.
    '''

    S = []
    for t in T:
        S.append(t)
        if not my_is_independent(S):
            S.remove(t)
    return S


def my_rank(L): 
    '''
    input: A list, L, of Vecs
    output: The rank of the list of Vecs
    '''

    L1 = L[:]
    L1 = subset_basis(L1)
    return len(L1)   

def direct_sum_decompose(U_basis, V_basis, w):
    '''
    input:  A list of Vecs, U_basis, containing a basis for a vector space, U.
    A list of Vecs, V_basis, containing a basis for a vector space, V.
    A Vec, w, that belongs to the direct sum of these spaces.
    output: A pair, (u, v), such that u+v=w and u is an element of U and
    v is an element of V.
    '''

    M = coldict2mat(U_basis + V_basis)
    temp = solve(M,w)
    len1 = len(U_basis)
    len2 = len(V_basis)
    Wu=Vec(set(range(len(U_basis))),{})
    Wv=Vec(set(range(len(V_basis))),{})
    for x in range(len1):
        Wu[x] = temp[x]
    for y in range(len2):
        Wv[y] = temp[len1 + y]
    U = coldict2mat(U_basis)
    V = coldict2mat(V_basis)
    a = U * Wu
    b = V * Wv
    return a,b


def is_invertible(M): 
    '''
    input: A matrix, M
    outpit: A boolean indicating if M is invertible.
    '''
    
    a = mat2coldict(M)
    b = mat2rowdict(M)
    if len(a) != len(b):
        return False
    a = [v for i,v in a.items()]
    return my_is_independent(a)    



def find_matrix_inverse(A):
    '''
    input: An invertible matrix, A, over GF(2)
    output: Inverse of A
    '''

    iden = Mat((A.D[0],A.D[0]),{(d,d):one for d in A.D[0]})
    coldiden = mat2coldict(iden)
    C = [solve(A,R[i]) for i in range(len(coldiden))]
    return coldict2mat(C)
