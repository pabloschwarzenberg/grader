def buscarTodas(a,b):
    
    lista = list(a)
    vacia = []
    
    
    for i in range(len(lista)):
        if lista[i] == b:
            cuenta = 0
            cuenta = lista.index(b,i)
            vacia.append(str(cuenta))
    
    j = (" ".join([str(i) for (i) in vacia]))
    return j
   
if __name__ == "__main__":
    oracion = input("Ingrese una oracion: ")
    letra = input("Ingrese una letra: ")
    
    print(buscarTodas(oracion,letra))