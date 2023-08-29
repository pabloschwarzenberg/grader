def palindromo(palabra):
    palabra2 = palabra[::-1]
    if palabra == palabra2:
        return True
    else:
        return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           