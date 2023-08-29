#Cálculo del dígito verificador de un rut
Rut = input()
Numero = 3
if len(Rut) == 7:
  Numero = 2
Total = 0
for digito in Rut: 
  x = int(digito) * Numero
  Total = Total + x
  Numero = Numero - 1
  if Numero == 1:
    Numero = 7
Entero = Total // 11
Resultado = Total - (11*Entero)
Verificador = 11-Resultado
if Verificador == 11:
  print("dv=0")
elif Verificador == 10:
  print("dv=k")
else:
  print("dv=" + str(Verificador))  