def es_secuencia_genoma(secuencia):
    '''Verifica si una secuencia es un genoma.'''
    letras_validas = set(['A', 'C', 'T', 'G'])
    secuencia_valida = all(letra.upper() in letras_validas for letra in secuencia)
    return secuencia_valida

secuencia = input("Ingrese la secuencia: ")
if es_secuencia_genoma(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
  