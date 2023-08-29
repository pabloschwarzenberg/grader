     def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    return True

# Ejemplo de uso
secuencia = input("Ingresa la secuencia de ADN: ")
if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
 