def decodificar(mensaje):
    if ((mensaje[1] == "1") and (mensaje[3] == "0")):
        return "hola"

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         