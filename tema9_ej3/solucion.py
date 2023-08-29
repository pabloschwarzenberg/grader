def decodificar(mensaje):
    letras=mensaje.split(",")
    s=""
    for letra in letras:
        n=int(letra,2)
        c=chr(n)
        s+=c
    return s

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)