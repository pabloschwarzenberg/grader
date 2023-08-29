def jerigonzo(string):
    lista = []
    lista3 = []
    vocales = ["a","e","i","o","u"]
    for a in string:
        lista.append(a)
    lista2 = lista.copy()
    for b in lista:
        print(b)
        if b in vocales:
            lista3.append(b)
            lista3.append("p")
            lista3.append(b)
        else:
            lista3.append(b)
    s = "".join(lista3)
    return s



if __name__ == "__main__":
  palabra = str(input("Ingrese su string "))
  print(jerigonzo(palabra))
  pass
         