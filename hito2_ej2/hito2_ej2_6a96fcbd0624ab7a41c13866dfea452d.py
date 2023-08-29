def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    return True


if __name__ == "__main__":
    secuencia = input()
    if validar_secuencia(secuencia):
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")