def validar_genoma(secuencia):
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}

    for letra in secuencia:
        if letra not in letras_validas:
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")

    if validar_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")

