#Cálculo del dígito verificador de un rut
a = str(input("Ingrese rut"))[::-1]
n = 2
b = 0
for i in a:
  if n == 8:
    n = 2
  b += int(i)*n
  n +=1
resto1 = b//11
resto2 = b - (11*resto1)
dv = 11- resto2
if dv == 10:
  dv = "k"
elif dv == 11:
  dv = 0
print("dv="+str(dv))



