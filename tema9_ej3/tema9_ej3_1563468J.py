def decodificar(mensaje):
    linea=mensaje.split(",")
    palabra=""
    n=0

    for i in linea:
        n=decimal(i)
        palabra+=chr(n)

    return palabra

def decimal(n):
    n=int(n,2)
    return n


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
