def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

secuencia_input = input("Ingrese la secuencia del genoma: ")

if es_secuencia_genoma(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")