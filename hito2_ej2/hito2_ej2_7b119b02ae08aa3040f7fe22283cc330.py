def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas
    nucleotidos_validos = {'A', 'C', 'T', 'G'}
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    
    return True


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia de ADN: ")
    
    if es_secuencia_genoma(secuencia):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")
      