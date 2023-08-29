#Cálculo del dígito verificador de un rut
n = [7, 6, 5, 4, 3, 2]
rut = input("Ingrese el rut:")
dv = 0
for i in rut[::-1]:
   dig = n.pop()
   dv += int(i) * dig
   n = [dig] + n
dv = 11 - (dv % 11)
if dv == 11:
   print("dv=", 0)
elif dv == 10:
   print("dv=", "K")
else:
   print("dv=", dv)

