def decodificar(mensaje):
    mensaje=mensaje.split(",")
    numeros=[]
    for i in mensaje[:]:
        numero=int(str(i),2)
        numeros.append(numero)
    mensaje=[]
    for j in numeros[:]:
        letra=chr(j)
        mensaje.append(letra)
    mensaje="".join(mensaje)
    return mensaje
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         