#Cálculo del dígito verificador de un rut
#Solicitar el numero de RUT al usuario
rut = input("Ingrese el numero de RUT (sin digito verificador): ")

#Calcular el digito verificador
suma = 0
multiplicador = 2

#Multiplicar cada digito por el multiplicador correspondiente y sumar los resultados
for digito in reversed(rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador == 8:
        multiplicador = 2

#Calcular el resto de la división por 11
resto = suma % 11

#Determinar el digito verificador
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = "0"
elif digito_verificador == 10:
    digito_verificador = "K"

#resultado
print("dv =", digito_verificador)
      