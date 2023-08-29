def decodificar(mensaje):
    mensaje = mensaje.replace(",","")
    cod = len(mensaje)//8
    i = 0
    j = 0
    k = 8
    lista = []
    lista2 = []
    
    while i < cod:
        js = mensaje[j:k]
        lista.append(js)
        j+= 8
        k+= 8
        i+=1
        
    for binario in lista:
        xp = int(binario,2)
        xp = chr(xp)
        lista2.append(xp)
        mensaje = "".join(lista2)

    return mensaje
         