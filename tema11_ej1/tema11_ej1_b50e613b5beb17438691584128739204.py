def palindromo(palabra):
    n = len(palabra)
    if n == 1:
        return True
    if palabra[0] == palabra[-1] and palindromo(palabra[1:n-1]) == True:
                                    return True
    else:
                                    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           