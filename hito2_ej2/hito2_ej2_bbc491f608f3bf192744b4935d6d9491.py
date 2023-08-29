secuencia = input("Ingrese la secuencia de ADN: ")
secuencia = secuencia.upper()

letras_validas = {'A', 'C', 'T', 'G'}
es_valida = all(letra in letras_validas for letra in secuencia)

if es_valida:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")