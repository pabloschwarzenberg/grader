N= eval(input("ingrese numero telefonico:"))
H= eval(input("ingrese hora de llamada:"))

if H >= 0 and H <= 7:
    print ("Resultado: CONTESTAR")
if H <= 14:
  digitos1 = N % 1000
  if digitos1 == 909:
    print("resultado: CONTESTAR")
if H >= 17 and H <= 19:
   digitos = N // 100000
   if digitos == 877:
    print ("reultado: NO CONTESTAR")
if H > 19:
    print("Resultado: NO CONTESTAR")