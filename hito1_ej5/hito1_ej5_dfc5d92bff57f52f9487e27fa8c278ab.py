#Cálculo del dígito verificador de un rut
print("Ingrese su RUT por favor (sin puntos ni el dígito verificador)")
print("Ejemplo; RUT = 12.345.678-9, escriba: 12345678")
#Ejemplo: 30686957

rut = str(input(": "))

n1 = eval(rut[7]) * 2
n2 = eval(rut[6]) * 3
n3 = eval(rut[5]) * 4
n4 = eval(rut[4]) * 5
n5 = eval(rut[3]) * 6
n6 = eval(rut[2]) * 7
n7 = eval(rut[1]) * 2
n8 = eval(rut[0]) * 3

suma = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
modulo = (suma % 11)
dv = 11 - modulo

if dv == 11:
    dv = 0
if dv == 10:
    dv = "k"

print("El dígito verificador es: {}".format(dv))
print("Su RUT es : {}".format(rut), dv, sep="-")