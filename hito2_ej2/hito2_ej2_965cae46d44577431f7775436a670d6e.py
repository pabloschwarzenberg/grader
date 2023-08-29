def validar_genoma(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True

# Ejemplo de uso
entrada = input("Ingrese la secuencia de ADN: ")
if validar_genoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
   