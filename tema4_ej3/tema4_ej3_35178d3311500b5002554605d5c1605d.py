def jerigonzo(string):
    lista= []
    for i in string:
      if i not in "aeiou":
        lista.append(i)
      else:
        lista.append(i)
        lista.append("p")
        lista.append(i)
    retorno = "".join(lista)
    return retorno


         