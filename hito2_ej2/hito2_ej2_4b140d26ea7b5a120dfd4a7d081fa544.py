def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return "secuencia incorrecta"

    # Si todas las letras son válidas, la secuencia es correcta
    return "secuencia correcta"

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    resultado = validar_secuencia_genoma(secuencia)
    print(resultado)