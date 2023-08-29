def es_secuencia_valida(secuencia):
    """
    Esta función recibe una secuencia de ADN en forma de string y devuelve True si es una secuencia válida, es decir,
    si contiene solamente las letras A, C, T y G (sin importar mayúsculas o minúsculas).
    """
    nucleotidos_validos = set(['A', 'C', 'T', 'G'])
    secuencia = secuencia.upper()  # Convertimos a mayúsculas para simplificar la validación
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return False
    return True


secuencia = input("Introduce la secuencia de ADN: ")
if es_secuencia_valida(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")