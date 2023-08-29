def validar_secuencia(secuencia):
    # Convertir la secuencia a minúsculas
    secuencia = secuencia.lower()
    
    # Verificar si la secuencia contiene caracteres no válidos
    caracteres_validos = {'a', 'c', 't', 'g'}
    for caracter in secuencia:
        if caracter not in caracteres_validos:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
