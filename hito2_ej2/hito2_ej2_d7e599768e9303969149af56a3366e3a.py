def es_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene únicamente las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia_input = input("Ingrese la secuencia: ")

# Validar la secuencia del genoma
if es_secuencia_genoma(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
    