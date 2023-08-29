#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut: "))

strRut = str(rut)
largoRut = len(strRut)
multiplicador = 2
sumadigito = 0
mod11 = 0
digito = 0



while largoRut>0:
    sumadigito = sumadigito + (int(strRut[largoRut-1])* multiplicador)

    multiplicador += 1

    if multiplicador>7:
        multiplicador=2

    largoRut -= 1


mod11 = sumadigito - ((sumadigito // 11) * 11)
digito = 11 - mod11

if digito == 11:
    print("dv=0")    
if digito == 10:
    print("dv=k")
else:
    print("dv="+str(digito))

      