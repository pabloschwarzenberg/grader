def decodificar(mensaje):
    mensaje=mensaje.split(",")
    numeros=[]
    for n in mensaje:
        y=int(str(n),2)
        numeros.append(y)
    letras=[]
    for i in numeros:
        y=chr(i)
        letras.append(y)
    palabras="".join(letras)
    return palabras