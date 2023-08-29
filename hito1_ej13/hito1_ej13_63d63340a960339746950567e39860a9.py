def numero_enteros(numero):
    lista = []
    i = 1
    if numero%i == 0 and numero > i:
        lista.append(numero/i)
        i += 1
    else:
        i += 1
    return lista

def factores(lista):
    i = 1
    lista2 = []
    while i < len(lista):
        for numero in range(lista):
            if numero%i == 0:
                lista2.append(numero/i)
                i += 1
            else:
                i +=1
    return lista
    
numero_enteros(int(input("ingrese usu número: ")))
