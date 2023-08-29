
def decodificar(mensaje):
    mensaje = mensaje.split(",")
    n1 = str(mensaje[0][:8])
    n2 = str(mensaje[1][:8])
    n3 = str(mensaje[2][:8])
    n4 = str(mensaje[3][:8])
    decimal1 = (int(str(n1), 2))
    decimal2 = (int(str(n2), 2))
    decimal3 = (int(str(n3), 2))
    decimal4 = (int(str(n4), 2))
    mensajehecho = chr(decimal1) + chr(decimal2) + chr(decimal3) + chr(decimal4)

 
    return mensajehecho

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         