def validar_genoma(secuencia):
    # Convertir la secuencia a minúsculas
    secuencia = secuencia.lower()

    # Verificar si la secuencia contiene caracteres inválidos
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    if validar_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")

