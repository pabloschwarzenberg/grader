def es_genoma(s):
  if sum([s.count(x) for x in ['A','T','G','C']]) == len(s):
    return 'Secuencia correcta'
  else:
    return 'Secuencia incorrecta'

genoma = input('')
genoma = es_genoma(genoma)
print(genoma)