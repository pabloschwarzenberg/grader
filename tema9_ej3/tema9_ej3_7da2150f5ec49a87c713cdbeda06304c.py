def decodificar(mensaj):
    mensaj=mensaj.split(",")
    numeros=[]
    letras=[]
    for elemento in range(len(mensaj)):
        numero=int((mensaj[elemento]), 2)
        numeros.append(numero)
    for elemento in range(len(numeros)):
        letra=chr(numeros[elemento])
        letras.append(letra)
    letras=''.join(letras)
    return letras
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
