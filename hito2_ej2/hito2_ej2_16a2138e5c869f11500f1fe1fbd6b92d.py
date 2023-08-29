def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para evitar distinguir entre mayúsculas y minúsculas
    for c in secuencia:
        if c not in "ACTG":
            return False
    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")

    if validar_secuencia_genoma(secuencia):
        print("La secuencia", secuencia, "es correcta")
    else:
        print("La secuencia", secuencia, "es incorrecta")