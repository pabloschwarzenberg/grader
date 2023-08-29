def validar_genoma(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False

    return True

# Solicitar al usuario que ingrese la secuencia de ADN
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia de ADN
if validar_genoma(secuencia):
    print("Secuencia correcta: la secuencia de ADN es válida.")
else:
    print("Secuencia incorrecta: la secuencia de ADN no es válida.")
