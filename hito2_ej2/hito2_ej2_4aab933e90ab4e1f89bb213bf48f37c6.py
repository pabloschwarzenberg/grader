def genoma(secuencia):
  while True:
    secuencia = input("genoma")
    for_s=len(secuencia)
      for x in  range(0,for_s):
        if chr(secuencia)==65 or chr(secuencia)==67 or chr(secuencia)==84 or chr(secuencia)==71:
          secuencia = True
   return secuencia