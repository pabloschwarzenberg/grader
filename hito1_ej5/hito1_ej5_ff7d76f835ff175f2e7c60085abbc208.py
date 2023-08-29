#Número verificador del rut

rut = input("Ingrese su RUT sin código verificador >>> ")

if len(rut) == 8:
    x1 = int(rut[7])*2
    x2 = int(rut[6])*3
    x3 = int(rut[5])*4
    x4 = int(rut[4])*5
    x5 = int(rut[3])*6
    x6 = int(rut[2])*7
    x7 = int(rut[1])*2
    x8 = int(rut[0])*3
    total = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

else:
    x1 = int(rut[6])*2
    x2 = int(rut[5])*3
    x3 = int(rut[4])*4
    x4 = int(rut[3])*5
    x5 = int(rut[2])*6
    x6 = int(rut[1])*7
    x7 = int(rut[0])*2
    total = x1 + x2 + x3 + x4 + x5 + x6 + x7

parteEntera = int(total/11)
resto = total - (11*parteEntera)
resultado = 11 - resto

if resultado == 11:
    print("dv =", str(0))
elif resultado == 10:
    print("dv = K")
else:
    print("dv =", str(resultado))