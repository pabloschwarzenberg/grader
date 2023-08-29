def decodificar(mensaje):
    pd = mensaje.split(",")
    for i in range(len(pd)):
        pd[i] = int(pd[i],2)
        pd[i] = chr(pd[i])
    return "".join(pd)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         