def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir todo a mayúsculas
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False  # La secuencia contiene un carácter inválido
    
    return True  # La secuencia es válida

# Pedir al usuario que ingrese la secuencia
secuencia_ingresada = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia_genoma(secuencia_ingresada):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")
     