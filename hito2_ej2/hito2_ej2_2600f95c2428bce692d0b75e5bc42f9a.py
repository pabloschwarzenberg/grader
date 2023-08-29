def validar_secuencia(secuencia):
    # Convertir la secuencia a letras mayúsculas para evitar distinción entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in "ACTG":
            return False

    return True

# Obtener la secuencia de ADN desde el usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia de ADN
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
