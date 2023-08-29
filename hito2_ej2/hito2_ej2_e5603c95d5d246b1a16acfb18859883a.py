def validar_genoma(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = {'A', 'C', 'T', 'G'}

    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False

    return True

secuencia_genoma = input("Ingrese la secuencia del genoma: ")

if validar_genoma(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")