#Cálculo del dígito verificador de un rut
rut = input("Ingrese su RUT: ")

if len(rut) == 8:
    n1 = int(rut[7])*2
    n2 = int(rut[6])*3
    n3 = int(rut[5])*4
    n4 = int(rut[4])*5
    n5 = int(rut[3])*6
    n6 = int(rut[2])*7
    n7 = int(rut[1])*2
    n8 = int(rut[0])*3
    total = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
else:
    n1 = int(rut[6])*2
    n2 = int(rut[5])*3
    n3 = int(rut[4])*4
    n4 = int(rut[3])*5
    n5 = int(rut[2])*6
    n6 = int(rut[1])*7
    n7 = int(rut[0])*2
    total = n1 + n2 + n3 + n4 + n5 + n6 + n7

entera = int(total/11)
resto = total - (11*entera)
resultado = 11 - resto

if resultado == 11:
    print("dv=" + str(0))
elif resultado == 10:
    print("dv=" + "K")
else:
    print("dv=" + str(resultado))