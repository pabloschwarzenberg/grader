def decodificar(mensaje):
    binarios = mensaje.split(",")
    l = (chr(int(num,2)) for num in binarios)
    return "".join(l)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         