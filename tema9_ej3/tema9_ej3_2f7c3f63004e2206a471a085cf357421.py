def decodificar(mensaje):
    #DECIMAL A BINARIO
    listaBin = mensaje.split(",")
    numeros = []
    separados = []
    for binario in listaBin:
        i = 0
        while i < len(binario):
            num = int(binario[i])
            agregar = num*2**(7 - i)
            numeros.append(agregar)
            i += 1
            if len(numeros) == 8:
                separados.append(numeros)
                numeros = []
    sumados = []
    for numeros in separados:
        suma = sum(numeros)
        sumados.append(suma)
    letras = []
    #RECIBE ENTERO DEVUELVE UN CARACTER
    for sumas in sumados:
        letra = chr(sumas)
        letras.append(letra)
    mensaje = ""
    for letra in letras:
        mensaje += letra           
            
    return mensaje