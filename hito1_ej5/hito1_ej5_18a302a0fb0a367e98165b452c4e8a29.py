#calculo del digito verificador de un rut
rut = input("Ingrese su rut sin digito verificador: ")
largo = len(rut)
suma = 0
digito = 0
mult = 2
while digito != largo:
    suma += int(rut[(largo - 1) - digito]) * mult
    mult += 1
    if mult == 8:
        mult = 2
    digito += 1
digito = 11 - (suma % 11)
if digito == 11:
    digito = 0
elif digito == 10:
    digito = "k"
print("dv={}".format(digito))