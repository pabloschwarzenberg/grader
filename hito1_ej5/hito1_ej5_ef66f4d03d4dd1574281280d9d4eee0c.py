rut = int((input("Ingrese el rut sin el digito verificador")))

rut0 = ((rut % 10) * 2)
rut1 = ((rut // 10 % 10) * 3)
rut2 = ((rut // 100 % 10) * 4)
rut3 = ((rut // 1000 % 10) * 5)
rut4 = ((rut // 10000 % 10) * 6)
rut5 = ((rut // 100000 % 10) * 7)
rut6 = ((rut // 1000000 % 10) * 2)
rut7 = ((rut // 10000000 % 10) * 3)
suma_rut = (rut0 + rut1 + rut2 + rut3 + rut4 + rut5 + rut6 + rut7)
print(suma_rut)
modulo_11 = suma_rut // 11
print(modulo_11)
x = suma_rut - (11*modulo_11)
print(x)
resultado = 11 - x
print(resultado)

if resultado == 11:
    print("dv= 0")
elif resultado == 10:
    print("dv= k")
else:
    print("dv=",resultado)