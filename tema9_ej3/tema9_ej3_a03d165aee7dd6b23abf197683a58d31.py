def decodificar(mensaje):
    lis1=mensaje.split(",")
    contador=0
    contador2=1
    lisDecimal=[]
    lisSumas=[]
    lisCaracteres=[]

    for i in range(0,len(lis1)):
        numero= lis1[i]
        for j in range (0, len(numero)):
            decimales=int(numero[-contador2])* 2 **contador
            lisDecimal.append(decimales)
            contador+=1
            contador2+=1
            if contador==8:
                suma=sum(lisDecimal)
                lisDecimal=[]
                contador=0
                contador2=1
                lisSumas.append(suma)
    for k in range(0,len(lisSumas)):
        caracter=chr(lisSumas[k])
        lisCaracteres.append(caracter)

    mensaje = "".join(lisCaracteres)
    return(mensaje)
