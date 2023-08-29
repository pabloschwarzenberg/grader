def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()
    
    # Comprobar si la secuencia contiene caracteres no válidos
    for nucleotido in secuencia:
        if nucleotido not in "ACTG":
            return False
    
    return True

# Obtener la secuencia de ADN desde el usuario
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia_genoma(secuencia_adn):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      