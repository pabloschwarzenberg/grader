def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:len(palabra)-2])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           