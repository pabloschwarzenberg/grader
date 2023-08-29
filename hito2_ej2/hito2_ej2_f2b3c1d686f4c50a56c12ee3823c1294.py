def es_genoma(secuencia):
    secuencia = secuencia.upper()
    
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

secuencia = input("Introduce la secuencia de ADN: ")

if es_genoma(secuencia):
    print("Secuencia correcta: representa un genoma")
else:
    print("Secuencia incorrecta: no representa un genoma")
      