def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    return True

secuencia = input('Ingresa la secuencia: ')
if es_secuencia_genoma(secuencia):
    print('secuencia correcta')
else:
    print('secuencia incorrecta')
