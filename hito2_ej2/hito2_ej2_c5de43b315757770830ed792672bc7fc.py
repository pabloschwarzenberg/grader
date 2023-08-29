 def validar_secuencia(secuencia):
    # Convertir la secuencia a letras mayúsculas
    secuencia = secuencia.upper()

    # Validar cada carácter de la secuencia
    for nucleotido in secuencia:
        if nucleotido not in ["A", "C", "T", "G"]:
            return False

    return True

# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
     