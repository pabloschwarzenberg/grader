def validar_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas
    
    for nucleotido in secuencia:
        if nucleotido not in 'ACTG':
            return False
    
    return True

# Pedir la entrada al usuario
secuencia_input = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia
if validar_genoma(secuencia_input):
    print("Secuencia correcta. Es un genoma válido.")
else:
    print("Secuencia incorrecta. No es un genoma válido.")
