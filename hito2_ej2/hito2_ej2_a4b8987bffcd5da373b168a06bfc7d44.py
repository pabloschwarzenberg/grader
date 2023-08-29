def es_secuencia_valida(secuencia):
    for letra in secuencia:
        if letra.upper() not in "ACTG":
            return False
    return True

secuencia = input("Ingresa una secuencia: ")
if es_secuencia_valida(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
     