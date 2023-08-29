def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in "ACTG":
            return False
    return True


secuencia = input("Ingrese la secuencia de ADN: ")


if validar_secuencia(secuencia):
    print("Secuencia correcta: representa un genoma")
else:
    print("Secuencia incorrecta: no representa un genoma")