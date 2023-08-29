#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número del RUT (sin dígito verificador): ")
factor = 2
suma = 0
for i in range(len(rut)-1, -1, -1):
   suma += int(rut[i]) * factor
   factor += 1
   if factor > 7:
     factor = 2
dv = 11 - (suma % 11)
if dv == 10:
   dv = "K"
elif dv == 11:
   dv = 0
print("dv =", dv)
2.3