rut = input("ingresa tu rut sin el numero verificador: ")
uno = rut[7]
dos = rut[6]
tres = rut[5]
cuatro = rut[4]
cinco = rut[3]
seis = rut[2]
siete = rut[1]
ocho = rut[0]

uno = int(uno)*2
dos = int(dos)*3
tres= int(tres)*4
cuatro = int(cuatro)*5
cinco = int(cinco)*6
seis = int(seis)*7
siete = int(siete)*2
ocho = int(ocho)*3

valor = uno + dos + tres + cuatro + cinco + seis + siete + ocho
modulo11 = int(valor / 11)
valor = valor - (11*modulo11)
resultado_f = 11-valor
digito_verificador = 0

if resultado_f == 11:
    digito_verificador = 0
elif resultado_f == 10:
    digito_verificador = "K"
else:
    digito_verificador = resultado_f
print("dv =",digito_verificador)