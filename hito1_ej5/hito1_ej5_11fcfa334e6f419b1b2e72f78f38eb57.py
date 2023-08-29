#Cálculo del dígito verificador de un rut
rut = int(input("ingrese rut sin el ultimo digito: "))

rutvuelta = str(rut)[::-1]

uno = int(rutvuelta[0])*2
dos = int(rutvuelta[1])*3
tres = int(rutvuelta[2])*4
cuatro = int(rutvuelta[3])*5
cinco = int(rutvuelta[4])*6
seis = int(rutvuelta[5])*7
siete = int(rutvuelta[6])*2
if(len(rutvuelta)==8):
    ocho = int(rutvuelta[7])*3
else:
    ocho = 0

suma = uno + dos + tres + cuatro + cinco + seis + siete + ocho
resto = suma%11

digitov = 11 - resto

if (digitov == 10):
    digitov = "k"
if ( digitov == 11):
    digitov = 0

print("digito verificador es: ", digitov)
    