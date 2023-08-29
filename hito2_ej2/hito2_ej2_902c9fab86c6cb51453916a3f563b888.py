   def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")   