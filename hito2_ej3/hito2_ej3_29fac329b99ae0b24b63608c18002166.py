def subsecuencias(secuencia, n):
    secuencia = str(secuencia)
    n = int(n)
    secuencias_todas = []
    secuencias_unicas = []
    for i in range((len(secuencia) - n + 1)):
        secuencia1 = ""
        for j in range(i, i + n):
            secuencia1 += secuencia[j]
            secuencias_todas.append(secuencia1.lower())
    for k in range(len(secuencias_todas)):
        veces = secuencias_todas.count(secuencias_todas[k])
        if veces == 1 and len(secuencias_todas[k]) == n:
            secuencias_unicas.append(secuencias_todas[k])
    if len(secuencias_unicas) > 0:        
      return print(secuencias_unicas)
    else:
      return print("['ninguna']")

q = str(input())
p = int(input())
subsecuencias(q, p)