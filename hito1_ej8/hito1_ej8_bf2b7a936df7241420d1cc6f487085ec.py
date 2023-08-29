#Descomponer un número
      
numero = str(input("Ingrese un numero: "))
unidad = int(numero[-1])
decena = int(numero[-2])
centena = int(numero[-3])
mil = int(numero[0])
digitacion = ""

if mil >=1:
  m = str(mil)+"M"+"+"
  digitacion = digitacion+m
else:
  print("No hay mil")
if centena >=1:
  c = str(centena)+"C"+"+"
  digitacion = digitacion+c
else:
  print("No hay centena")
if decena >=1:
  d = str(decena)+"D"+"+"
  digitacion = digitacion+d
else:
  print("No hay decena")
if unidad >=1:
  u = str(unidad)+"U"
  digitacion = digitacion+u
else:
  print("No hay unidad")


print(digitacion)