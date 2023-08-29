def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in nucleotidos_validos:
            return False
    
    return True

secuencia_genoma = input("Ingrese la secuencia del genoma: ")

if es_secuencia_genoma(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      