def rot13(palabra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    resultado = ""
    for i in palabra :
        if i <= alfabeto[12] :
            resultado += alfabeto[alfabeto.index(i)+13]
        else :
            resultado += alfabeto[alfabeto.index(i)-13]
    return resultado


           