#Cálculo del dígito verificador de un rut
# Solicitar al usuario ingresar el número del RUT
rut = input("Ingrese el número del RUT (sin dígito verificador): ")

# Verificar que el RUT ingresado contenga solo dígitos numéricos
if not rut.isdigit():
    print("El RUT debe contener solo dígitos numéricos.")
else:
    # Invertir el RUT y convertirlo en una lista de dígitos
    rut_invertido = list(reversed(rut))
    
    # Multiplicar cada dígito del RUT por un factor y sumar los resultados
    factor = 2
    suma = 0
    for digito in rut_invertido:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    # Calcular el dígito verificador restando el módulo 11 de la suma a 11
    digito_verificador = 11 - (suma % 11)
    
    # Manejar casos especiales para el dígito verificador
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    
    # Imprimir el resultado
    print("dv =", digito_verificador)
     