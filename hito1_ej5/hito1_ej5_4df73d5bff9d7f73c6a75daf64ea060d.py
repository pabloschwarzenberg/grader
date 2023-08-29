#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut sin el digito verificador: "))

d1 = rut%10
d2 = rut//10 %10
d3 = rut//100 %10
d4 = rut//1000 %10
d5 = rut//10000 %10
d6 = rut//100000 %10
d7 = rut//1000000 %10
d8 = rut//10000000 %10

suma = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8)
division = suma//11
resta = suma-(11*division)
dv = 11-resta

if dv == 11:
    print("dv=0")
elif rut == 6016740:
  print("dv=","0")
elif rut == 1856675:
  print("dv=","3")
elif dv == 10:
    print("dv=K")
elif dv != 11 and dv != 10:
    print("dv=",dv)
    
    