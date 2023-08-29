def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    return True

entrada = input("Ingrese la secuencia: ")
if es_secuencia_genoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      