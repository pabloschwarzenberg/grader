def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas

    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False

    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    if validar_secuencia_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")

