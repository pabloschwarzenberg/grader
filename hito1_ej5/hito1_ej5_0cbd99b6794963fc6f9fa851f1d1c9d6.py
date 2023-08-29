#Cálculo del dígito verificador de un rut
   
rut = eval(input("igresar rut "))
Fac = "32765432"
indice = len(Fac) - 1
suma = 0

while rut > 0:
  digito = rut % 10
  suma = suma + (digito * int(Fac[indice]))
  rut = rut // 10
  indice = indice - 1
x = suma % 11
dv = 11 - x
if dv == 11:
  print("dv = 0")
elif dv == 10:
  print("dv = K")
else:
  print("dv= ", dv)