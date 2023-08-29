def validar_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    return True

entrada = input("Ingrese la secuencia del genoma: ")
if validar_genoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      