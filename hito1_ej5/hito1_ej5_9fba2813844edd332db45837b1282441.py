#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut: ")

if len(rut) == 7:

  rut = "0"+rut

multiplicaciones = []

multiplicador = 3



for i in rut:

  resultado = int(i)*multiplicador

  multiplicaciones.append(resultado)

  multiplicador-=1

  if multiplicador == 1:

    multiplicador = 7

final = 0



for i in multiplicaciones:

  final += i



restar = final//11

print(restar)

total = final-(restar*11)

digito = 11 - total



if digito == 11:

  digito = 0

elif digito == 10:

  digito = "K"



print("dv="+str(digito))      