def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas

    for letra in secuencia:
        if letra not in 'ACTG':
            return False
    
    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    
    if validar_secuencia(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")