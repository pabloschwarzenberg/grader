def subsecuencia_de_ADN(secuencia,n):
    lista = list(secuencia)
    print("lista: ",lista)
    lista.append(lista[0])
    print("lista non: ",lista)
    lista = lista[::-1]
    lista = lista[0:-1]
    lista = lista[::-1]
    print("lista modificada: ",lista)
    lista2 = ["C","G","A"]
    fila = []
    fila2 = []
    fila3 = []
    fila4 = []
    contador = 0
    for i in range(len(lista)):
        if(contador == n):
            print(lista[i])
            fila2.append(lista[i])
        if(contador != n):
            fila.append(lista[i])
            print(lista[i])
            contador = contador + 1
        
    print("JODERMACHOOOOOOOOOO",fila)

    print("POFNERIBVIEV",lista2[0])
    for i in range(len(lista2)):
        if(fila == lista2):
            aprobar = 1
            print("APROBADO",lista2)
            break
        else:
            aprobar = 0
            print("RECHAZADO",lista2)
            break
    for i in range(len(lista2)):
        if(fila2 == lista2):
            aprobar2 = 1
            print("APROBADO2",lista2)
            break
        else:
            aprobar2 = 0
            print("RECHAZADO2",lista2)
            break

    if(aprobar == aprobar2 and fila == fila2):
        for i in range(len(fila2)):
            if(fila2[i] == "C"):
                fila3.append("G")
            elif(fila2[i] == "G"):
                fila3.append("A")
            elif(fila2[i] == "A"):
                fila3.append("C")
        print(fila)
        print(fila3)
        fila = "".join(fila)
        fila3 = "".join(fila3)
        fila = fila.lower()
        fila3 = fila3.lower()
        print(fila)
        print(fila3)
        return [fila,fila3]
    else:
        return ["ninguna"]
    
secuencia = input("Ingrese una subsecuencia de ADN: ")
n = int(input("Ingrese un numero entero"))
print(subsecuencia_de_ADN(secuencia,n))