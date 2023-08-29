def decodificar(mensaje):
    mensaje ="1101000,1101111,1101100,1100001"
    lista1 = mensaje.split(",")
    for i in lista1:
        a = int(i,2)
        b = chr((a),end="")
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         