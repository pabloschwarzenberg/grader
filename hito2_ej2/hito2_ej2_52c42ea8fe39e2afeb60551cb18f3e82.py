def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a minúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.lower()

    # Verificar si la secuencia contiene solamente las letras A, C, T, G
    for caracter in secuencia:
        if caracter not in ['a', 'c', 't', 'g']:
            return False

    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese una secuencia: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      