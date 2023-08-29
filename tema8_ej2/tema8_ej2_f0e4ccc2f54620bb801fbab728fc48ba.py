def buscarTodas(a,b):
  A = list(a)
  B = list(b)
  C = []
  i = 0
  while i < len(A):
    if b in A[i]:
      C.append(i)
      i += 1
    else:
      i += 1
  return " ".join(str(index) for index in C)
