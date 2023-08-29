abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedarioMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def rot13(Palabra, Avance):
    Clave = ''
    Tope = len(abecedarioMayus)
    Posicion = 0
    for letra in Palabra:
        for i in range(Tope):
            if (i + Avance < Tope):
                Posicion = i + Avance
            else:
                Posicion = abs((Tope - i) - Avance)
            if letra == abecedario[i]:
                Clave = Clave + abecedario[Posicion]
            elif letra == abecedarioMayus[i]:
                Clave = Clave + abecedarioMayus[Posicion]
    return Clave    