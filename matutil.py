from vec import Vec
from mat import Mat

def identity(D, one):
  """
  Given a set D and the field's one, returns the DxD identity matrix
  """
  return Mat((D,D), {(d,d):1 for d in D})

def keys(d):
  """
  Given a dict, returns something that generates the keys; given a list,
     returns something that generates the indices.  Intended for coldict2mat and rowdict2mat.
  """
  return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
  """
  Given either a dict or a list, returns one of the values.
     Intended for coldict2mat and rowdict2mat.
  """
  return next(iter(d.values())) if isinstance(d, dict) else d[0]

def mat2rowdict(A):
  """
  Given a matrix, return a dictionary mapping row labels of A to rows of A
	"""
  return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}

def mat2coldict(A):
  """
  Given a matrix, return a dictionary mapping column labels of A to columns of A
  """
  return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def coldict2mat(coldict):
    """
    Given a dictionary or list whose values are Vecs, returns the Mat having these
    Vecs as its columns.  This is the inverse of mat2coldict.
    """
    row_labels = value(coldict).D
    return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})

def rowdict2mat(rowdict):
    """
    Given a dictionary or list whose values are Vecs, returns the Mat having these
    Vecs as its rows.  This is the inverse of mat2rowdict.
    """
    col_labels = value(rowdict).D
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})

def listlist2mat(L):
  """Given a list of lists of field elements, return a matrix whose ith row consists
  of the elements of the ith list.  The row-labels are {0...len(L)}, and the
  column-labels are {0...len(L[0])}
  """
  m,n = len(L), len(L[0])
  return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

