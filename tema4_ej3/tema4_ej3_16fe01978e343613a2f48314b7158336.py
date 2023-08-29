def jerigonzo(string):
    lista = []
    for letra in string:
        lista.append(letra)
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i])
        if lista[i]=="a" or lista[i]=="e" or lista[i]=="i" or lista[i]=="o" or lista[i]=="u":
            lista2.append("p")
            lista2.append(lista[i])
            
    cadena = "".join(lista2)
    return cadena

if __name__ == "__main__":
    pass
         