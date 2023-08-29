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

suma = (d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3)
division = suma//11
resta = suma-(11*division)
dv = 11-resta

if dv == 11:
    print("dv=0")
elif dv == 10:
    print("dv=K")
elif dv != 11 and dv != 10:
    print("dv=",dv)
