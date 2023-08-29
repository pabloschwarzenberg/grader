def es_secuencia_genomica(secuencia):
    bases_validas = set(['A', 'C', 'T', 'G'])
    secuencia_valida = all(base.upper() in bases_validas for base in secuencia)
    return secuencia_valida


if __name__ == '__main__':
    secuencia = input("Introduce una secuencia de ADN: ")
    if es_secuencia_genomica(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
