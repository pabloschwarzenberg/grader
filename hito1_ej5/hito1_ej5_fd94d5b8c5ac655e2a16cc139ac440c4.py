def calcular_digito_verificador(rut):
    """
    Función para calcular el dígito verificador de un número de RUT utilizando el algoritmo Módulo 11.

    Argumento:
    - rut: número de RUT sin el dígito verificador

    Retorna:
    - dv: dígito verificador calculado
    """
    rut = str(rut)  # Convertir el RUT a una cadena de texto

    # Paso 1: Calcular la suma ponderada de los dígitos del RUT
    factor = 2
    suma_ponderada = 0
    for i in range(len(rut)-1, -1, -1):
        suma_ponderada += int(rut[i]) * factor
        factor = factor + 1 if factor < 7 else 2

    # Paso 2: Calcular el dígito verificador como el complemento a 11 del resto de la división por 11
    resto = suma_ponderada % 11
    dv = 11 - resto if resto != 0 else '0'
    dv = 'K' if dv == 10 else str(dv)

    return dv

# Solicitar al usuario ingresar un número de RUT
rut = input("Ingrese un número de RUT (sin el dígito verificador): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv =", digito_verificador)




      