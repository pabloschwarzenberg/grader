def es_secuencia_genoma(secuencia):
    """Función que valida si una secuencia dada es una secuencia de genoma"""
    for nucleotido in secuencia:
        if nucleotido.upper() not in ["A", "C", "T", "G"]:
            return False
    return True
secuencia = input("Ingrese la secuencia a validar: ")
if es_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")