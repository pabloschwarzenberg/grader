def validar_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas
    for letra in secuencia:
        if letra not in "ACTG":
            return False
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")