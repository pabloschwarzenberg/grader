def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas
    
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    
    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    
    if es_secuencia_genoma(secuencia) == "ACTG" or "actg":
        print("correcta")
    else:
        print("incorrecta")