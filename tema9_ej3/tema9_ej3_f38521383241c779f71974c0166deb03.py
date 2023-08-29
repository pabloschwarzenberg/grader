def decodificar(mensaje):
    dec = str(mensaje, 2)
    return dec

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         