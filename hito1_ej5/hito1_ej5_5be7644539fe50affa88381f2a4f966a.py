#Cálculo del dígito verificador de un rut
RUT = input("ingrese RUT: ")
if (len(RUT)==8):
  numer1 = RUT[7]
  a = int(numer1) * 2
  numer2 = RUT[6]
  b = int(numer2) * 3
  numer3 = RUT[5]
  c = int(numer3) * 4
  numer4 = RUT[4]
  d = int(numer4) * 5 
  numer5 = RUT[3]
  e = int(numer5) * 6
  numer6 = RUT[2]
  f = int(numer6) * 7
  numer7 = RUT[1]
  g = int(numer7) * 2
  numer8 = RUT[0]
  h = int(numer8) *3
  suma = a + b + c + d + e + f + g + h
  division = suma /11
  resultado = suma - (11 * int(division))
  dv = 11 - resultado
  if (dv==11):
    dv = 0
  if (dv==10):
    dv = str("k")

if (len(RUT)==7):
  numer1 = RUT[6]
  a = int(numer1) * 2
  numer2 = RUT[5]
  b = int(numer2) * 3
  numer3 = RUT[4]
  c = int(numer3) *  4
  numer4 = RUT[3]
  d = int(numer4) * 5 
  numer5 = RUT[2]
  e = int(numer5) * 6
  numer6 = RUT[1]
  f = int(numer6) * 7
  numer7 = RUT[0]
  g = int(numer7) * 2
  suma = a + b + c + d + e + f + g
  division = suma /11
  resultado = suma - (11 * int(division))
  dv = 11 - resultado
  if (dv==11):
    dv = 0
  if (dv==10):
    dv = str("k")
print("dv = ", dv)