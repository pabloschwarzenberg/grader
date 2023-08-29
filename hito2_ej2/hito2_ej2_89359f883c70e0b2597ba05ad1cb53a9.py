def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in 'ACTG':
            return False
    return True

secuencia = input("Ingresa la secuencia del genoma: ")
if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
