def palindromo(palabra):

    palabra = list(palabra)
    if len(palabra) == 1:
        return True

    elif len(palabra) == 2:
        if palabra[0] == palabra[-1]:
            return True
        else: return False 

    else: # Palabra con mas de 2 espacios
        if palabra[0] == palabra[-1]:
            return palindromo(palabra[1:-1])
        else:
            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           