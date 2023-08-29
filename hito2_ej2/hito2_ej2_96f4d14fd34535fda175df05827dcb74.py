def es_secuencia_genoma(secuencia):
    # Convertir la secuencia a letras mayúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene solo A, C, T, y G
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Solicitar al usuario que ingrese la secuencia
secuencia_ingresada = input("Ingrese la secuencia de ADN: ")

# Verificar si la secuencia es un genoma válido
if es_secuencia_genoma(secuencia_ingresada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      