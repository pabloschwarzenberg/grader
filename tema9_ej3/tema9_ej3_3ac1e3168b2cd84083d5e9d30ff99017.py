def decodificar(mensaje):
  x = str(mensaje[0:8])

  decimal1=(int(str(x), 2))

  letra1=chr(decimal1)

  y = str(mensaje[10:17])

  decimal2=(int(str(y), 2))

  letra2=chr(decimal2)

  z = str(mensaje[19:26])

  decimal3=(int(str(z), 2))

  letra3=chr(decimal3)

  a = str(mensaje[28:35])

  decimal4=(int(str(a), 2))

  letra4=chr(decimal4)

  palabra = letra1+letra2+letra3+letra4

  return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    chr.mensaje
    print(mensaje)
    
