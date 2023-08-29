
rut=int(input("ingrese su rut sin digito: "))
rut=str(rut)
rut=rut[::-1]
for digito in rut:
    for j in range(1,8):
        print(digito*j)