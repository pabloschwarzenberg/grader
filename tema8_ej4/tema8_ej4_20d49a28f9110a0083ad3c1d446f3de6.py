def rot13(Palabra):
    Resultado = ""
    for Caracter in Palabra:
        if 'a' <= Caracter <= 'z':
            N_caracter = chr((ord(Caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= Caracter <= 'Z':
            N_caracter = chr((ord(Caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            N_caracter = Caracter
        Resultado += N_caracter
    return Resultado