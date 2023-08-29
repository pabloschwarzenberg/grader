secuencia = input()
letra = ""

for i in range(0, len(secuencia)):
  letra = secuencia[i]
  if(letra != "A" and letra != "C" and letra != "T" and letra != "G" and letra != "a" and letra != "c" and letra != "t" and letra != "g"):
    print("secuencia incorrecta")
    break
  elif(i == len(secuencia)-1 ):
    print("correcta")