def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    if not secuencia.isalpha():
        return False
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    return True


if __name__ == "__main__":
    secuencia = input("Ingresa la secuencia de ADN: ")
    if es_secuencia_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
      