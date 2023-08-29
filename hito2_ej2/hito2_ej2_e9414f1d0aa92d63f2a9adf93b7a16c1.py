      def validar_secuencia(secuencia):
    # Convertir la secuencia a minúsculas
    secuencia = secuencia.lower()

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False

    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")

    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
