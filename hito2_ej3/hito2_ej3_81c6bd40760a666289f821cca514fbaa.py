      def ordenados(cadena):
    n = len(cadena)
    cadena = cadena.upper()
    validos = 'ACTG'
    pares = 0

    
    i = 0
    while not (i >= (n - 1)):
        elemento = cadena[i]
        elemento2 = cadena[i + 1]
        if (elemento <= elemento2):
            pares = pares + 1
        i = i + 1

    
    noADN = 0
    i = 0
    while not (i >= n):
        elemento = cadena[i]
        if not (elemento in validos):
            noADN = noADN - 1
        i = i + 1

    
    if (noADN < 0):
        pares = noADN

    return (pares)