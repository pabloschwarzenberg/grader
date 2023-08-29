def es_genoma(secuencia):
    secuencia = secuencia.upper() # convertimos a mayúsculas
    letras_validas = set('ACGT')
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    return True

secuencia = input("Introduce la secuencia: ")
if es_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
