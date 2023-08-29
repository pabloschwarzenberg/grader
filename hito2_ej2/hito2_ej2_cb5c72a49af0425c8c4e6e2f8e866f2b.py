# secuencia

valido = "ACTG"
es_valido = 1

secuencia = input("Ingrese una secuencia: ")

secuencia = secuencia.upper()
for c in secuencia:
    if valido.find(c) == -1:
        es_valido = 0
        break

if es_valido == 0:
    print("\nLa secuencia es incorrecta! No es valida")
else:
    print("\nLa secuencia es correcta! Si es valida")