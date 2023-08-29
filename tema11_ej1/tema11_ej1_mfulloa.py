def palindromo(palabra):
    palabra=list(palabra)
    if palabra[0]!=palabra[len(palabra)-1]:
        return False    
    return True

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           