#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut: ")

largo_rut = len(rut)
ultima_posicion = largo_rut - 2
suma = 0
multiplicador = 2

#Procesamiento
while ultima_posicion >= 0:
    multiplicacion = int(rut[ultima_posicion]) * multiplicador
    suma += multiplicacion
    if multiplicador == 7:
        multiplicador = 2
    else:
        multiplicador += 1
    ultima_posicion -= 1

variable_intermedia = (suma // 11) * 11
resta = abs(suma - variable_intermedia)
digito_verificador_calculado = 11 - resta

if digito_verificador_calculado == 11:
    digito_verificador_calculado = 0
elif digito_verificador_calculado == 10:
    digito_verificador_calculado = "k"

#Salida
print("El dígito verificador es:", str(digito_verificador_calculado))