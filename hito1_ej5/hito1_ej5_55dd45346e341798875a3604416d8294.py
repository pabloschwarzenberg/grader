#Cálculo del dígito verificador de un rut
rut = (input("Ingrese su RUT:"))
n = 1
sum = 0
for i in rut[::-1]:
  if n >= 2 and n <7: 
    n += 1
  else:
    n=2
  producto = int(i) * n
  sum +=producto
resto = sum -(11 *(sum // 11))
dv = 11 - resto
if dv == 11:
  dv = 0
elif dv == 10:
  dv = "K"
else:
  dv = dv
print("dv="+str(dv))