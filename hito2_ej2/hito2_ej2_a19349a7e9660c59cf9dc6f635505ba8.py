def es_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in 'ACTG':
            return False
    
    return True

# Solicitar la secuencia al usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if es_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")     