def validarSecuenciaGenoma(secuencia):
    secuencia = secuencia.upper()

    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False

    return True

entrada = input("Ingrese la secuencia del genoma: ")

if validarSecuenciaGenoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")