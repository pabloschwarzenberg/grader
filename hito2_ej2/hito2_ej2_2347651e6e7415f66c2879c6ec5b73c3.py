def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for base in secuencia:
        if base not in ['A', 'C', 'T', 'G']:
            return False

    return True


secuencia_input = input("Ingrese la secuencia de ADN: ")


if validar_secuencia(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")