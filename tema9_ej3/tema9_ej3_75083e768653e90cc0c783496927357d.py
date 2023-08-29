def decodificar(mensaje):
    p=mensaje.split(",")
    pal=""
    for x in p:
          pal+=chr(int(x[:8], 2))
    return pal
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         