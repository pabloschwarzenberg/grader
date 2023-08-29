#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut: "))
a = rut // 10000000 * 3
b = rut // 1000000 % 10 * 2
c = rut // 100000 % 10 * 7
d = rut // 10000 % 10 * 6
e = rut // 1000 % 10 * 5
f = rut // 100 % 10 * 4
g = rut // 10 % 10 * 3
h = rut // 1 % 10 * 2
suma = a + b + c + d + e + f + g + h
producto = suma % 11
resta = 11 - producto
if resta == 11:
      print("dv=" + str(0))
elif resta == 10:
      print("dv=K")
else:
      print("dv=" + str(resta))