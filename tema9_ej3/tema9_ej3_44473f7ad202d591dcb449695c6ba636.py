def decodificar(mensaje):

    primera = str(mensaje[0:8]) #primeros 8 números
    decimal1=(int(str(primera), 2))
    letra1=chr(decimal1)
    #-----------------------------------------------------------
    segunda = str(mensaje[10:17]) #segundos 8 números
    decimal2=(int(str(segunda), 2))
    letra2=chr(decimal2)
    #-----------------------------------------------------------
    tercera = str(mensaje[19:26]) #terceros 8 números
    decimal3=(int(str(tercera), 2))
    letra3=chr(decimal3)
    #-----------------------------------------------------------
    cuarta = str(mensaje[28:35]) #cuartos 8 números
    decimal4=(int(str(cuarta), 2))
    letra4=chr(decimal4)
    #-----------------------------------------------------------
    palabra = letra1+letra2+letra3+letra4
    return palabra