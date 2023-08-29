"""
separador = " "  # Necesitamos un separador para cuando decodifiquemos esto


def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)


def binario_a_ascii(binario):
    # Convertir binario a decimal
    valor = int(binario, 2)
    # Convertir el decimal a su representación ASCII
    return chr(valor)


def texto_a_binario(texto):
    texto_binario = ""  # El resultado
    contador = 0
    for letra in texto:
        texto_binario += ascii_a_binario(letra)
        # Agregar un espacio entre binarios, excepto si es el último carácter
        if contador + 1 < len(texto):
            texto_binario += separador
        contador += 1
    return texto_binario


def binario_a_texto(texto_binario):
    texto_plano = ""
    for binario in texto_binario.split(separador):
        texto_plano += binario_a_ascii(binario)
    return texto_plano


"""
    Modo de uso
"""

texto_original = "Parzibyte"
texto_codificado = texto_a_binario(texto_original)
print(f"El texto '{texto_original}' es '{texto_codificado}' en binario")
# Decodificar
original = binario_a_texto(texto_codificado)
print(f"El texto binario '{texto_codificado}' es '{original}'")