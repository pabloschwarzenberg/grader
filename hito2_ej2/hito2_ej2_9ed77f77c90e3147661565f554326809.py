def es_secuencia_genoma(secuencia):
    secuencia = secuencia.lower()
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False
    return True

secuencia = input("Ingrese la secuencia de ADN: ")

if es_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
