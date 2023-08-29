def decodificar(mensaje):
    return mensaje
def decodificar(mensaje):

  a = str(mensaje[0:8])

  decimal1=(int(str(a), 2))

  letra1=chr(decimal1)

  b = str(mensaje[10:17])

  decimal2=(int(str(b), 2))

  letra2=chr(decimal2)

  c = str(mensaje[19:26])

  decimal3=(int(str(c), 2))

  letra3=chr(decimal3)

  d = str(mensaje[28:35])

  decimal4=(int(str(d), 2))

  letra4=chr(decimal4)

  palabra = letra1+letra2+letra3+letra4

  return palabra



if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)