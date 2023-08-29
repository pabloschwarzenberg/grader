def decodificar(mensaje):

    mensaje=mensaje.split(",")
    a = []
    for n in mensaje:
        aux=int(n,2)
        letras=chr(aux)
        a.append(letras)
    a="".join(a)
    return a 
if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)