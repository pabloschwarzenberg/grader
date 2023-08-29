def jerigonzo(string):
  stringreturn = ""
  contador = 0
  while len(string) > contador:
    if string[contador] == "a" or string[contador] == "e" or string[contador] == "i" or string[contador] == "o" or string[contador] == "u":
        stringreturn = stringreturn +string[contador] + "p" + string[contador]
    else:
        stringreturn = stringreturn + string[contador]
    contador = contador + 1

  return stringreturn