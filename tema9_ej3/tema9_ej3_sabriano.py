def decodificar(mensaje):
    lista=mensaje.split(",")
    decimal=[]
    for i in lista:
        a=int(i,2)
        decimal.append(a)
    letras=[]
    for j in decimal:
        b=chr(j)
        letras.append(b)
    palabra="".join(letras)
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         