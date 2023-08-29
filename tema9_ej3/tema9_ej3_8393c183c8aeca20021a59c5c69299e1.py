def decodificar(mensaje):
    
    codigo1 = str(mensaje[0:8])
    decimal1=(int(str(codigo1), 2))
    primera_letra=chr(decimal1)
    
    codigo2 = str(mensaje[10:17])
    decimal2=(int(str(codigo2), 2))
    segunda_letra=chr(decimal2)
    
    codigo3 = str(mensaje[19:26])
    decimal3 = (int(str(codigo3), 2))
    tercera_letra = chr(decimal3)
    
    codigo4 = str(mensaje[28:35])
    decimal4 = (int(str(codigo4), 2))
    cuarta_letra = chr(decimal4)
    
    palabra = primera_letra+segunda_letra+tercera_letra+cuarta_letra
    return palabra