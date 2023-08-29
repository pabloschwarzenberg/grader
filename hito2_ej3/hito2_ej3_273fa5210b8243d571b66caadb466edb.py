def nucleotidos(str, n):
    # ACGACG -> CGA GAC
    i = 0

    secuencias_unicas_candidatos = []
    secuencias_repetidas = []
    while n <= len(str):
        bases = str[i:n]
        if not bases in str[i+1:]:
            secuencias_unicas_candidatos.append(bases)
        elif bases in str[i+1:]:
            secuencias_repetidas.append(bases)
        i += 1
        n += 1
    for elem in secuencias_repetidas:
        if elem in secuencias_unicas_candidatos:
            secuencias_unicas_candidatos.remove(elem)

    secuencias_unicas = secuencias_unicas_candidatos
    for elemento in secuencias_unicas:
        print(elemento)
    if len(secuencias_unicas) == 0:
        print('ninguna')

r=input('Secuencia: ')
n=int(input('Número de bases: '))
nucleotidos(r,n)

