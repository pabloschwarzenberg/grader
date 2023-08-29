#Cálculo del dígito verificador de un rut
 rut = int(input("ingreese su rut "))
d8 = rut//10000000
rest = (rut%10000000)
rut = rest
d7 = rut//1000000
rest = (rut%1000000)
rut = rest
d6 = rut//100000
rest = (rut%100000)
rut = rest
d5 = rut//10000
rest = (rut%10000)
rut = rest
d4 = rut//1000
rest = (rut%1000)
rut = rest
d3 = rut//100
rest = (rut%100)
rut = rest
d2 = rut//10
rest = (rut%10)
rut = rest
d1 = rest
suma = 3*d8 + 2*d7 + 7*d6 + 6*d5 + 5*d4 + 4*d3 + 3*d2 + 2*d1
resto = suma%11
dv = 11 - resto
if dv==11:
    print(0)
else:
    if dv==10:
        print("k")
    else:
        print(dv)    