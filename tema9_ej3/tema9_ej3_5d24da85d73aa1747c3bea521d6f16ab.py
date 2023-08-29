def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len(numeroBin) - 1
    for i in numeroBin:
        decimal += (int(i) * 2 ** (exp))
        exp = exp - 1
    return decimal


def decodificar(mensaje):
    mensaje=mensaje.split(",")
    palabra=""
    for i in mensaje:
        i = str(i)
        x = aDecimal(i)
        x=chr(x)
        x=str(x)
        palabra+=x

    return palabra




if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         