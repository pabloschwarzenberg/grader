def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    letras_permitidas = {'A', 'C', 'T', 'G'}
    for letra in secuencia:
        if letra not in letras_permitidas:
            return False
    return True

# Obtener la secuencia del usuario
secuencia_input = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia_input):
    print("Secuencia correcta: representa un genoma")
else:
    print("Secuencia incorrecta: no representa un genoma")
