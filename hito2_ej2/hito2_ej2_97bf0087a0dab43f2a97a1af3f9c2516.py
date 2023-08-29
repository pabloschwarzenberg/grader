def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    
    # Verificar si la secuencia contiene caracteres que no son A, C, T o G
    for letra in secuencia:
        if letra not in "ACTG":
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")      