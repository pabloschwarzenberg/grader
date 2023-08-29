rut = int(input("ingrese su rut sin dv: "))
print(rut)
multi = 2
suma = 0

while rut > 0:
    ult_digito =rut %10
    producto = multi * ult_digito
    suma = suma + producto
    print("ultimo digito =", ult_digito)
    print("producto =", producto)
    rut = rut // 10
    multi = multi + 1
    if multi == 8:
        multi = 2
print ("suma =", suma)
resultado = 11 - (suma % 11)
print ("resultado =", resultado )

if resultado == 11:
    print ("dv = 0")
elif resultado == 10:
    print ("dv = K")
else:
    print ("dv =", resultado)

      