#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut sin el digito verificador \n")
suma=0
if len(rut)==8:
 r1 = int(rut[0]) * 3
 r2 = int(rut[1]) * 2
 r3 = int(rut[2]) * 7
 r4 = int(rut[3]) * 6
 r5 = int(rut[4]) * 5
 r6 = int(rut[5]) * 4 
 r7 = int(rut[6]) * 3
 r8 = int(rut[7]) * 2
 suma = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
elif len(rut)==7:
 r1 = int(rut[0]) * 2
 r2 = int(rut[1]) * 7
 r3 = int(rut[2]) * 6
 r4 = int(rut[3]) * 5
 r5 = int(rut[4]) * 4
 r6 = int(rut[5]) * 3
 r7 = int(rut[6]) * 2
 suma = r1 + r2 + r3 + r4 + r5 + r6 + r7
 

modulo = suma % 11

digito = 11 - modulo

if digito == 11:
    print("dv=0")
else:
    if digito == 10:
        print("dv=K")
    else:
        print("dv={}".format(digito))