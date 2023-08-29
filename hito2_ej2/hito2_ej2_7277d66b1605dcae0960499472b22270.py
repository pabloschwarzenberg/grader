def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas

    for nucleotido in secuencia:
        if nucleotido not in "ACTG":
            return False

    return True

# Ejemplo de uso
secuencia_input = input("Ingrese la secuencia de ADN: ")
if validar_secuencia(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
