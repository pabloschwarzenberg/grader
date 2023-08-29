def decodificar(mensaje):
    mensaje = mensaje.replace(",","")
    regla1 = []
    regla2 = []
    regla3 = ""
    n = 0
    x = 0
    y = 8
    while n < int(len(mensaje)/8):
        regla1.append(mensaje[x:y])
        n+=1
        x+=8
        y+=8
    for x in regla1:
        regla2.append(int(str(x), 2))
    for i in regla2:
        regla3 = regla3 + str(chr(i))
    return regla3
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)