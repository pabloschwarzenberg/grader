def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    return True

input_secuencia = input("Introduce la secuencia del genoma: ")
if validar_secuencia(input_secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
