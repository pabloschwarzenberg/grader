def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas
    
    for nucleotido in secuencia:
        if nucleotido not in "ACTG":  # Verificar si el nucleótido no es válido
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
