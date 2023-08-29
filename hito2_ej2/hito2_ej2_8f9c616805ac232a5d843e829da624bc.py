if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}
    if all(letra in letras_validas for letra in secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
