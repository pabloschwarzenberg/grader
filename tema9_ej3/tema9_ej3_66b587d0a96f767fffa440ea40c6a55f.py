def decodificar(mensaje):
    a = str(mensaje[0:8])
    deci1 = (int(str(a), 2))
    le1 = chr(deci1)
    b = str(mensaje[10:17])
    deci2 = (int(str(b), 2))
    le2 = chr(deci2)
    c = str(mensaje[19:26])
    deci3 = (int(str(c), 2))
    le3 = chr(deci3)
    d = str(mensaje[28:35])
    deci4 = (int(str(d), 2))
    le4 = chr(deci4)
    palabra = le1 + le2 + le3 + le4
    return palabra
if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
  