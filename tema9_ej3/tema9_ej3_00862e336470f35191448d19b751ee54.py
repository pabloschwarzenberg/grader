def decodificar(mensaje):
    a = str(mensaje[0:8])
    decima11 = (int(str(a), 2))
    letra1=chr(decima11)
    b = str(mensaje[10:17])
    decima12=(int(str(b), 2))
    letra2=chr(decima12)
    c = str(mensaje[19:26])
    decima13=(int(str(c), 2))
    letra3=chr(decima13)
    d = str(mensaje[28:35])
    decima14=(int(str(d), 2))
    letra4=chr(decima14)
    palabra = letra1+letra2+letra3+letra4
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)