def es_secuencia_genoma(secuencia):
    # Convertir la secuencia a minúsculas
    secuencia = secuencia.lower()

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for nucleotido in secuencia:
        if nucleotido not in ['a', 'c', 't', 'g']:
            return False

    return True

# Pedir al usuario que ingrese una secuencia
secuencia_ingresada = input("Ingrese una secuencia de ADN: ")

# Validar la secuencia ingresada
if es_secuencia_genoma(secuencia_ingresada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
