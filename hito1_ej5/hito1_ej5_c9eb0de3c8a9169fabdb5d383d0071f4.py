#Cálculo del dígito verificador de un rut

def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)
    factor = 2
    suma = 0
    
    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor = factor + 1 if factor < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "dv=0"
    elif digito_verificador == 10:
        return "dv=K"
    else:
        return "dv=" + str(digito_verificador)

rut_input = input("Ingrese el número de RUT (sin guiones ni dígito verificador): ")

resultado_dv = calcular_digito_verificador(rut_input)

print(resultado_dv)