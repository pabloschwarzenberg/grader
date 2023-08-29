#Cálculo del dígito verificador de un rut
rut =input("Rut: ")

total= 0
total = total + int(rut[-1] ) * 2
total = total + int(rut[-2] ) * 3
total = total + int(rut[-3] ) * 4
total = total + int(rut[-4] ) * 5
total = total + int(rut[-5] ) * 6
total = total + int(rut[-6] ) * 7
total = total + int(rut[-7] ) * 2
if len(rut) >= 8:
  total = total + int(rut[-8] ) * 3


a = total % 11
b = 11 - a

if b == 11:
  print("Dv = 0")
elif b == 10:
  print("Dv = K")
else:
  print("Dv = ",b)

