#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su Rut(solo 8 primeras cifras): "))

#Procedimiento de calculo
a = (((rut % 10)// 1) * 2)
b = (((rut % 100)// 10) * 3)
c = (((rut % 1000)// 100) * 4)
d = (((rut % 10000)// 1000) * 5)
e = (((rut % 100000)// 10000) * 6)
f = (((rut % 1000000)// 100000) * 7)
g = (((rut % 10000000)// 1000000) * 2)
h = (((rut % 100000000)// 10000000) * 3)

x = a + b + c + d + e + f + g + h

y = (x // 11)

z = x - (11*y)

digito = (11 - z)

if digito == 11:
    print("dv= 0 ")
elif digito == 10:
    print("dv= K ")
else:
    print("dv=",digito)     