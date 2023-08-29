def buscarTodas(a,b):
    a.lower
    b.lower
    posiciones=""
    indice=0
    while indice != -1:
        if(a.find(b, indice) != -1):
            posiciones+=' '+str(a.find(b, indice))
        indice=a.find(b, indice)
        if(indice == 0):
            indice+=1
        else:
            if(indice != -1):
                indice+=1

    return posiciones.lstrip('  ')


if __name__ == "__main__":
    a = input("Ingresa una frase: ")
    b = input("Ingresa la palabra buscada: ")
    posiciones  = buscarTodas(a,b)
    print("La palabra se encuentra en posiciones: ",posiciones)
           