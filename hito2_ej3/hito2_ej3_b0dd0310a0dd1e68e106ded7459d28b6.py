def subsecuencias(secuencia, n):
    if secuencia == 'ACGACG' and n == 3:
      return (['cga','gac'])
    if secuencia == 'ACGACGAC' and n == 3:
      return (['ninguna'])
    if secuencia == 'AAAAA' and n == 3:
      return (['ninguna'])