def decodificar(mensaje):
    lista1=mensaje.split(",")
    cont=0
    cont2=1
    listaDecimal=[]
    listaSumas=[]
    listaCaracteres=[]

    for i in range(0,len(lista1)):
        numero= lista1[i]
        for j in range (0, len(numero)):
            decimales=int(numero[-cont2])* 2 **cont
            listaDecimal.append(decimales)
            cont+=1
            cont2+=1
            if cont==8:
                suma=sum(listaDecimal)
                listaDecimal=[]
                cont=0
                cont2=1
                listaSumas.append(suma)
    for k in range(0,len(listaSumas)):
        caracter=chr(listaSumas[k])
        listaCaracteres.append(caracter)

    mensaje = "".join(listaCaracteres)
    return(mensaje)

         