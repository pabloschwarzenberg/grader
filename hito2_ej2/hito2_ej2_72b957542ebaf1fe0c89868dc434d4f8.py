def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    valid_chars = {'A', 'C', 'T', 'G'}  # Conjunto de caracteres válidos

    for char in secuencia:
        if char not in valid_chars:
            return False  # La secuencia contiene un caracter no válido

    return True  # Todos los caracteres son válidos


if __name__ == "__main__":
    secuencia = input("Ingresa la secuencia del genoma: ")

    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
      