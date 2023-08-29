def palindromo(palabra):
    L = len(palabra)
    if L == 1:
        return True
    if palabra[0] == palabra[-1] and palindromo(palabra[1:L-1]) == True:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           