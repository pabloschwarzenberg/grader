def decodificar(mensaje):
    x = mensaje.split(",")
    mensaje_final = ""
    for i in x:
        decimal = int(i,2)
        mensaje_final+=chr(decimal)
    return mensaje_final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
