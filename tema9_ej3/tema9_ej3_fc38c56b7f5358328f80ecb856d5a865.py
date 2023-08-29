def decodificar(mensaje):
    letras_binario = mensaje.split(",")
    lista_decimal=[]
    letras =[]
    for i in letras_binario:
        suma=0
        n=len(i)
        for j in i:
            if j == "1":
                suma+=2**(n-1)
            n-=1
        lista_decimal.append(suma)
    for i in lista_decimal:
        letras.append(chr(i))
    palabra="".join(letras)

    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         