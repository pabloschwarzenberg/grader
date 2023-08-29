#Cálculo del dígito verificador de un rut
def digito_verificador(rut):
    digito_reservado = str(rut)[::-1]
    factores = 2
    suma = 0
    for digito in digito_reservado:
        suma += int(digito) * factores
        factores += 1
        if factores >7:
            factores =2

    digito_veri = 11 - (suma % 11)
    if digito_veri == 11:
        return 0
    elif digito_veri == 10:
        return "K"
    else:
        return digito_veri
rut = int(input("Ingrese el nuemro del rut sin el digito verficador: "))
dv = digito_verificador(rut)
print("dv=",dv)
