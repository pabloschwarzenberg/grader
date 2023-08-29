def decodificar(mensaje):
    a = mensaje.split(",")
    b = list(a)
    c = ""
    for i in b:
      c+=chr(int(i, 2))
    return c

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         