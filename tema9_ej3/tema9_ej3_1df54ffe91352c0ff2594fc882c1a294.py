def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
  
def decodificar(mensaje):
    a = str(mensaje[0:8])
    decimal_1 = (int(str(a), 2))
    letra_1 = chr(decimal_1)
    b = str(mensaje[10:17])
    decimal_2 = (int(str(b), 2))
    letra_2 = chr(decimal_2)
    c = str(mensaje[19:26])
    decimal_3 = (int(str(c), 2))
    letra_3 = chr(decimal_3)
    d = str(mensaje[28:35])
    decimal_4 = (int(str(d), 2))
    letra_4 = chr(decimal_4)
    palabra = letra_1 + letra_2 + letra_3 + letra_4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)