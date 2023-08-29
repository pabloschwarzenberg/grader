def validar_secuencia(secuencia):
    secuencia = secuencia.upper()

    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False

    return True

secuencia = input("Ingrese la secuencia de ADN: ")

if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")