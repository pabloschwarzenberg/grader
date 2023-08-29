def verificar_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    
    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return "secuencia incorrecta"
    
    return "secuencia correcta"

# Solicitar la secuencia al usuario
secuencia = input("Ingrese la secuencia: ")

# Verificar la secuencia del genoma
resultado = verificar_genoma(secuencia)

# Imprimir el resultado
print(resultado)