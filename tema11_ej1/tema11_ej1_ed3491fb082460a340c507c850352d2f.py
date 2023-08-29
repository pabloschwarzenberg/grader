def palindromo(palabra):
    letras = []
    for letra in palabra:
        letras.append(letra)
    if len(letras) == 1:
        return 
    if letras[0] != letras[-1]:
        return False
    else:
        letras.remove(letras[0])
        letras.pop()
        palabra ="".join(letras)
        palindromo(palabra)
    return True


if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           