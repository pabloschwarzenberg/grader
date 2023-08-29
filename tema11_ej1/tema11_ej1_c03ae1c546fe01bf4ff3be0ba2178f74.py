def palindromo(palabra):
    print(palabra[0])
    print(palabra[-1])
    if len(palabra)<2:
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        palabra = palabra[1:-1]
        print(palabra)
        palindromo(palabra)
    return True


if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
