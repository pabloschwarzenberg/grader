def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir todo a mayúsculas
    
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Pedir la secuencia al usuario
secuencia_input = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia
if validar_secuencia(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")