def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas
    
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

# Programa principal
secuencia = input("Ingrese la secuencia del genoma: ")

if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta. Representa un genoma válido.")
else:
    print("Secuencia incorrecta. No representa un genoma válido.")      