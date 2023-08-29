def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    nucleotidos_validos = set(['A', 'C', 'T', 'G'])
    
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos_validos:
            return "La secuencia es incorrecta"
    
    return "La secuencia es correcta"


def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)


if __name__ == "__main__":
    secuencia_adn = input("Ingrese una secuencia de ADN: ")
    resultado_secuencia = validar_secuencia(secuencia_adn)
    print(resultado_secuencia)
    
    frase = input("Ingrese una frase: ")
    cantidad_palabras = contar_palabras(frase)
    print("La frase tiene", cantidad_palabras, "palabras.")
