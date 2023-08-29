def decodificar(mensaje):
    a=mensaje.split(",")
    i=0
    lista_potencias=[]
    while i<8:
        potencia=2**(i)
        lista_potencias.append(potencia)
        i+=1

    


    lista1=[]
    for elemento in a:
        lista2=[]
        j=0
        while j<8:
            resultado=int(elemento[j])*lista_potencias[7-j]
            lista2.append(resultado)
            j+=1
        lista1.append(lista2)


    letras=[]
    for listabebe in lista1:
        suma=0
        k=0
        while k<8:
            suma+=listabebe[k]
            k+=1
        letras.append(suma)


    mensaje=""
    for elemento in letras:
        x=chr(elemento)
        mensaje+=x

        
    return(mensaje)
