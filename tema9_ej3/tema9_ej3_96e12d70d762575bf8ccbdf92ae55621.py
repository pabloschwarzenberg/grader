def decodificar(mensaje):
  abc1 = str(mensaje[0:8])
  primdec =(int(str(abc1), 2))
  letra1 = chr(primdec)
  abc2 = str(mensaje[10:17])
  segdec =(int(str(abc2), 2))
  letra2 = chr(segdec)
  abc3 = str(mensaje[19:26])
  terdec = (int(str(abc3), 2))
  letra3 = chr(terdec)
  abc4 = str(mensaje[28:35])
  cuardec = (int(str(abc4), 2))
  letra4 = chr(cuardec)
  frase = letra1+letra2+letra3+letra4
  return frase

if __name__=="__main__":
  mensaje = decodificar("01101000,01101111,01101100,01100001")
  print(mensaje)
