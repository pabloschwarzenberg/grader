#Cálculo del dígito verificador de un rut
RUT = eval(input("Ingrese un rut sin el digito verificador: "))

a = (RUT // 10000000) * 3
b = ((RUT // 1000000) % 10) * 2
c = ((RUT // 100000) % 10) * 7
d = ((RUT // 10000) % 10) * 6
e = ((RUT // 1000) % 10) * 5
f = ((RUT // 100) % 10) * 4
g = ((RUT // 10) % 10) * 3
h = ((RUT // 1) % 10) * 2

suma = (a + b + c + d + e + f + g + h)
divicion = (suma // 11)
resto = suma - (11 * divicion)
resta = (11 - resto)

if (resta == 11):
    print("dv= ", 0)
elif (resta == 10):
    print("dv= ", "K")
else:
    print("dv= ", resta)