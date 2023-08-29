def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    if secuencia.isalpha() and all(letra in "ACTG" for letra in secuencia):
        return "secuencia correcta"
    return "secuencia incorrecta"

secuencia = input("Introduce la secuencia: ")
resultado = validar_secuencia(secuencia)
print(resultado)
