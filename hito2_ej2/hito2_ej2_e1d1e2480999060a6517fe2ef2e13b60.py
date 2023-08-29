def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  
    for nucleotido in secuencia:
        if nucleotido not in 'ACTG':
            return False
    return True

secuencia_input = input("Introduce la secuencia de ADN: ")

if es_secuencia_genoma(secuencia_input):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")