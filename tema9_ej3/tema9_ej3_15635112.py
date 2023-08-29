def decodificar(mensaje):
    letras=mensaje.split(",")
    print(letras)
    palabra=""
    for i in range(len( letras)):
        print(letras[i])
        numero=0
        for j in range(len(letras[i])):
            print(letras[i][j])
            numero=numero+(int(letras[i][j])*(2**((len(letras[i]))-j-1)))
            print(numero)
        letra=chr(numero)
        palabra=palabra+letra
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         