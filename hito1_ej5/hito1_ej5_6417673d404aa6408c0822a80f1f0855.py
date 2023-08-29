def calcular_digito_verificador(rut):
    rut = rut.replace(".", "")  # Eliminar puntos del RUT si los hay
    rut_reversed = rut[::-1]  # Invertir el RUT
    multiplicador = [2, 3, 4, 5, 6, 7]
    suma = 0

    for i in range(len(rut_reversed)):
        digito = int(rut_reversed[i])
        multiplicando = multiplicador[i % 6]
        suma += digito * multiplicando

    resto = suma % 11
    resultado = 11 - resto if resto != 0 else 0

    if resultado == 10:
        return "k"
    else:
        return str(resultado)

# Programa principal
rut = input("Ingrese el RUT (sin guión ni dígito verificador): ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
