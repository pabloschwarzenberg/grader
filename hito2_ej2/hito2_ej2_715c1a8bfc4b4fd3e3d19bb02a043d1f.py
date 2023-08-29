def validar_secuencia_adn(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True

secuencia_adn = input("Ingrese la secuencia de ADN: ")

if validar_secuencia_adn(secuencia_adn):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
