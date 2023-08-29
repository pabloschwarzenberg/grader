def palindromo(palabra):
    if len(palabra) == 1:
        return True
    if palabra[0] == palabra[len(palabra)-1]:
        cont = 0
        n = ""
        for letra in palabra:
            if cont > 0 and cont < len(palabra)-1:
                n += letra
            cont += 1
        if palindromo(n):
            return True
    return False



if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
    print(palindromo("roror"))