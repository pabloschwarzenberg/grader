def decodificar(mensaje):
    letras=mensaje.split(",")
    numeros=[]
    for n in letras:
        y=int(str(n),2)
        numeros.append(y)
    mensaje=[]
    for n in numeros:
        y=chr(n)
        mensaje.append(y)
    mensaje="".join(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         