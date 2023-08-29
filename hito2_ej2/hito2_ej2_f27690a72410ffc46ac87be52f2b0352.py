def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True

# Obtener la secuencia de ADN desde el usuario
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia de ADN
if validar_secuencia(secuencia_adn):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
