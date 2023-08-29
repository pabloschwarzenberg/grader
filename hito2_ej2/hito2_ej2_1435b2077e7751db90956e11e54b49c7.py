def es_genoma(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar que la secuencia solo contenga las letras A, C, T, G
    for letra in secuencia:
        if letra not in "ACTG":
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")

    if es_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
