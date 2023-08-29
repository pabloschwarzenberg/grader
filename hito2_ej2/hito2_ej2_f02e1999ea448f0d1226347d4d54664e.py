def es_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    for char in secuencia:
        if char not in ['A', 'C', 'T', 'G']:
            return False
    return True


secuencia = input("Ingrese la secuencia de ADN: ")


if es_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")      