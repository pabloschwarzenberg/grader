rut = input("Escriba su rut sin digito verificador: ")
suma=0
multi= 2
for r in rut [::-1]:
    suma += int (r) * multi
    multi += 1
    if multi == 8:
        multi = 2
resto = suma % 11
resta = 11 - resto
if resta == 11:
    print ("El digito verificador de su rut es: 0")
elif resta == 10:
    print ("El digito verificador de su rut es: k")
else:
    print ("dv=",resta)
