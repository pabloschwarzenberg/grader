def palindromo(palabra):
    if len(palabra) >= 3:
        if palabra[0] == palabra[len(palabra)-1]:
           return palindromo(palabra[1:len(palabra)-1])
    if len(palabra) == 2:
        if palabra[0] == palabra[1]:
            return True
    if len(palabra) == 1:
        return True

    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           