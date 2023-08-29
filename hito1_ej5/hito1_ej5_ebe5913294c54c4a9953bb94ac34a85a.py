#Cálculo del dígito verificador de un rut
Rut = input("Ingrese RUT sin dv: ")
Rutl = len(Rut)

Total = 0
Total = Total + 2*int(Rut[-1])
Total = Total + 3*int(Rut[-2])
Total = Total + 4*int(Rut[-3])
Total = Total + 5*int(Rut[-4])
Total = Total + 6*int(Rut[-5])
Total = Total + 7*int(Rut[-6])
Total = Total + 2*int(Rut[-7])
if Rutl == 8:
  Total = Total + 3*int(Rut[-8])

resto = Total % 11
dv = 11 - resto
if dv == 10:
  print("dv=K")
elif dv == 11:
 print("dv=0")
else:
 print("dv=",dv)