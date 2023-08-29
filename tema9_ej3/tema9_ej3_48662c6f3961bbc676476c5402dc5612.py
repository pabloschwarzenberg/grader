def decodificar(mensaje):
    decimal = []
    numeros = mensaje.split(",")

    for j in range(len(numeros)):
        lista = list((numeros[j]))
        for i in range(len(lista)):
            lista[i] = int(lista[i]) * 2**(len(lista)-1-i)

        decimal.append(sum(lista))


    for i in range(len(decimal)):
        decimal[i] = chr(decimal[i])
        
    mensaje = ''.join(decimal)
    return mensaje
