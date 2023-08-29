def jerigonzo(string):
    lista = list(string)
    for i in range(len(string)):
        if lista[i] == "a":
            lista[i] = "apa"
        elif lista[i] == "e":
            lista[i] = "epe"
        elif lista[i] == "i":
            lista[i] = "ipi"
        elif lista[i] == "o":
            lista[i] = "opo"
        elif lista[i] == "u":
            lista[i] = "upu"
    return "".join(lista)
  
         