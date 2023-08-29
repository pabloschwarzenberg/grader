def rot13(palabra):
  abc = "abcdefghijklmnopqrstuvwxyz"
  string = ''
  for i in range(len(palabra)):
    indice = abc.index(palabra[i])
    if indice >= 13:
      string = string + abc[indice+13-26]
    else:
      string = string + abc[indice+13]
  return string
