def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    
    return True

# Solicitar secuencia de ADN al usuario
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia(secuencia_adn):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")
      