def palindromo(palabra):
    if palabra[0] == palabra[-1]:
        central = palabra[1:-1]
        if len(palabra) < 4:
            return True
        parcial = palindromo(central)
        return parcial
    else:
        return False


if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
