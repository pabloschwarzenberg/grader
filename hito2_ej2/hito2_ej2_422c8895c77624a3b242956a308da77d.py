def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in "ACTG":
            return "secuencia incorrecta"
    return "secuencia correcta"

secuencia = input("Ingrese la secuencia del genoma: ")
print(validar_secuencia_genoma(secuencia))     