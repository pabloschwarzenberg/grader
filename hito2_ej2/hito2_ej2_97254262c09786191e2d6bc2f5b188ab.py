def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene únicamente las letras A, C, T y G
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese una secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")
