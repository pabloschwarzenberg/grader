def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for nucleotido in secuencia:
        if nucleotido not in 'ACTG':
            return False
    return True

# Solicitar al usuario la secuencia de ADN
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia de ADN
if es_secuencia_genoma(secuencia_adn):
    print("Secuencia correcta. Podría representar un genoma.")
else:
    print("Secuencia incorrecta. No es válida para un genoma.")
