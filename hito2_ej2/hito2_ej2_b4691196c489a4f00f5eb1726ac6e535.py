def es_genoma(secuencia):
    """
    Verifica que la secuencia ingresada sea una secuencia válida del genoma (contiene solamente las letras A,C,T,G).
    """
    for letra in secuencia.upper():
        if letra not in ["A", "C", "T", "G"]:
            return False
    return True

# Entrada del usuario
secuencia = input("Ingresa una secuencia: ")

# Validación de la secuencia
if es_genoma(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
