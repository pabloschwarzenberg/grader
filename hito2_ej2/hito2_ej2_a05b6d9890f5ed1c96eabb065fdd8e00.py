def validar_genoma(secuencia):
    # Convertir la secuencia a mayúsculas para comparar sin distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in "ACTG":
            return False

    return True

if __name__ == "__main__":
    # Leer la secuencia de ADN ingresada por el usuario
    secuencia = input("Ingrese la secuencia de ADN: ")

    # Validar la secuencia de ADN
    if validar_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")