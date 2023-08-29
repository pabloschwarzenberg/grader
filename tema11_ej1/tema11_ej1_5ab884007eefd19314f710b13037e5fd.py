def palindromo(palabra):
  palabra=list(palabra)
  for i in range(0,len(palabra)):
    if palabra[i]==palabra[len(palabra)-1-i]:
      continue
    else:
      return False
  return True