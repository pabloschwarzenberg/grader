def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}

    for letra in secuencia:
        if letra not in letras_validas:
            return False

    return True

secuencia = input("Ingrese la secuencia de ADN: ")

if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
