def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()
    
    # Verificar si la secuencia contiene caracteres no válidos
    for nucleotido in secuencia:
        if nucleotido not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

if __name__ == "__main__":
    # Leer la secuencia desde la entrada estándar
    secuencia = input("Ingrese la secuencia de ADN: ")
    
    # Validar la secuencia
    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
