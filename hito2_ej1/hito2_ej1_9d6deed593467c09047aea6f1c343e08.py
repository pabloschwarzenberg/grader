def alinear(secuencia1, secuencia2):
  align = ""
  i = 0
  for letra in secuencia1:
    if letra == secuencia2[i]:
      align += letra
    else:
      align += "_"  
      i += 1
      return align

secuencia1 = input("Ingresa la primera secuencia de ADN: ")
secuencia2 = input("Ingresa la segunda secuencia de ADN: ")

align = alinear(secuencia1, secuencia2)

print(align)