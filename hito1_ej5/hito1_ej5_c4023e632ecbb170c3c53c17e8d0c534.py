#Cálculo del dígito verificador de un rut
rut = input("Escriba su rut sin digito verificador: ")
suma = 0
multi = 2
for i in rut [::-1]:
    suma += int (i) * multi
    multi += 1
    if multi == 8:
        multi = 2
resto = suma % 11
resta = 11 - resto
if resta == 11:
    print("dv=0")
elif resta ==10:
    print("dv=k")
else:
    print("dv=%d"%(resta))      