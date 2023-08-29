def palindromo(palabra):
  if palabra[0] == palabra[-1]:
    if len(list(palabra)) == 3:
      return True
    h = list(palabra)
    b= len(list(palabra))
    c= b//2
    if palabra[0:c+1] == palabra[c:b]:
      return True
    else:
      return False
  else:
    return False
           