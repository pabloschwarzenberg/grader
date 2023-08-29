def jerigonzo(string):
    lista = []
    for i in string:
        lista.append(i)
    pal=""
    vocal =["a","e","i","o","u"]
    cont=0
    for x in lista:
        if lista[cont] in vocal:
            pal = pal + lista[cont]+"p"+lista[cont]
        else:
            pal = pal + lista[cont]
        cont=cont+1
    
    return pal

      