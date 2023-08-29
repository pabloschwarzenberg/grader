#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    # Convertir el RUT a una lista de dígitos
    digitos = [int(d) for d in str(rut)]
    # Lista de factores para calcular el dígito verificador
    factores = [2, 3, 4, 5, 6, 7, 2, 3]
    # Calcular el producto de cada dígito por su factor correspondiente
    productos = [a * b for a, b in zip(digitos[::-1], factores)]
    # Sumar todos los productos
    suma = sum(productos)
    # Calcular el dígito verificador como el complemento de la suma módulo 11
    digito_verificador = 11 - (suma % 11)
    # Casos especiales para dígitos verificadores mayores a 9
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0
    return digito_verificador
# Solicitar al usuario ingresar el RUT sin dígito verificador
rut = int(input("Ingrese el RUT sin dígito verificador: "))
# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)
# Imprimir el resultado
print("dv=" + str(dv))