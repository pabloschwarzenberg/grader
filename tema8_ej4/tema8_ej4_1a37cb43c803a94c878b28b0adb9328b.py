def rot13(palabra):
    """
    Esta función recibe una palabra y la retorna encriptada con el algoritmo rot13.
    """
    abc = "abcdefghijklmnopqrstuvwxyz"  # al abecedario original
    nueva_palabra = ""  # variable para almacenar la palabra encriptada
    for letra in palabra:
        if letra.lower() in abc:  # solo se encriptan las letras del abecedario
            nueva_pos = (abc.index(letra.lower()) + 13) % 26  # nueva posición
            nueva_letra = abc[nueva_pos]
            # mantiene la mayúscula o minúscula original
            if letra.isupper():
                nueva_letra = nueva_letra.upper()
            nueva_palabra += nueva_letra
        else:
            # si no es una letra del abecedario, se conserva tal cual
            nueva_palabra += letra
    return nueva_palabra

if __name__ == "__main__":
    palabra = input("Ingrese la palabra que quiere encriptar: ")
    palabra_encriptada = rot13(palabra)
    print("La palabra encriptada es:", palabra_encriptada)          