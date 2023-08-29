def validar_secuencia(secuencia):
    secuencia = SECUENCIA.UPPER()  

    for letra in secuencia:
        if letra not in "ACTG":
            return False

    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")

