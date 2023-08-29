#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut sin número verificador:")
digits = list(rut)
num = 2
suma = 0
for i in range(len(digits)):
  suma += int(digits[len(digits)-(i+1)]) * num
  if num < 7:
    num += 1
  else:
    num = 2
resto = suma%11
verificador = 11-resto
if verificador == 11:
  verificador = 0
if verificador == 10:
  verificador = 'k'
print("dv=",verificador)      