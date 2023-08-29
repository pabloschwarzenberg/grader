  def validar_secuencia:
    # Convertir la secuencia a minúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.lower()
    
    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False
    
    return True

# Obtener la secuencia de ADN desde el usuario
secuencia = input("Ingresa la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
    