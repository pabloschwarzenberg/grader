def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    letras_validas = set("ACTG")  # Conjunto de letras válidas

    for letra in secuencia:
        if letra not in letras_validas:
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
