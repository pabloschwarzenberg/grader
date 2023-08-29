def validador_secuencias(secuencia):
    a_secuencia = secuencia.lower()
    caracteres_validos = ['a','c','t','g']
    secuencia_analisis = []
    for base in secuencia:
        if bool(base in caracteres_validos == True):
            secuencia_analisis.append(base)
    if len(secuencia_analisis) != len(list(secuencia)):
        return print('secuencia incorrecta')
    elif len(secuencia_analisis) == len(list(secuencia)):
        return print('secuencia correcta')
secuencia = str(input())
validador_secuencias(secuencia)
