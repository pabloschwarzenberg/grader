def palindromo(palabra):
    if len(palabra) == 1:
        return True

    elif len(palabra) == 2:
        if palabra[0] == palabra[-1]:
            return True
        else:
            return False

    else:
        if palindromo(palabra[1:-1]) and palabra[0] == palabra[-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
