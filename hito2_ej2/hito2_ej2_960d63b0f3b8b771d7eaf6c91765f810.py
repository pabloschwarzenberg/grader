def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas

    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False

    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")

    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
