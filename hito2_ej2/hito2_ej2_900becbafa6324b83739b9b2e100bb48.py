def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = set(['A', 'C', 'T', 'G'])
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True

# Solicitar al usuario la secuencia de ADN
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia e imprimir el resultado
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
