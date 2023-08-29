def validar_genoma(secuencia):
    secuencia = secuencia.upper()

    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return "secuencia incorrecta"

    return "secuencia correcta"


if __name__ == "__main__":
    secuencia = input("Ingresa la secuencia de ADN: ")
    resultado = validar_genoma(secuencia)
    print(resultado)
