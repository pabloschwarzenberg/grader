def jerigonzo(a):
  vocales = "aeiou"
  Vocales = list(vocales)
  A = list(a)
  J = []
  i = 0
  while i < len(A):
    if A[i] in Vocales:
      J.append("{}p{}".format(A[i], A[i]))
      i += 1
    else:
      J.append("{}".format(A[i]))
      i += 1
  return "".join(str(letra) for letra in J)        