rut = eval(input("rut "))
factores = "32765432"
indice = len(factores) - 1
suma = 0
while rut > 0:
  digito = rut % 10
  suma = suma + (digito * int(factores[indice])) 
  rut = rut // 10
  indice = indice - 1
resto = suma % 11
dv = 11 - resto
if dv == 11:
  print("dv = 0")
elif dv == 10:
  print("dv = K")
else:
  print("dv = ", dv)