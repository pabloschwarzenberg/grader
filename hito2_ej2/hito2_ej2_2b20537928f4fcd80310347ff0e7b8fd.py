def es_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in "ACTG":
            return False
    return True

secuencia = input("Ingrese una secuencia: ")

if es_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
