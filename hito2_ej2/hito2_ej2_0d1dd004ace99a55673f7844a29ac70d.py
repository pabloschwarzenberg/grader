def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar cada caracter de la secuencia
    for caracter in secuencia:
        if caracter not in ["A", "C", "T", "G"]:
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")

    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
