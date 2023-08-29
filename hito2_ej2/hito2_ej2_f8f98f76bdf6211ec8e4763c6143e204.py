def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True


# Solicitar la entrada al usuario
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")