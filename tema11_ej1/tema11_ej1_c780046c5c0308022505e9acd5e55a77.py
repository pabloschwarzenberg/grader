def palindromo(palabra):
    if len(palabra)>1:
        if palabra[0]!=palabra[-1]:
            return False
        else:
            palabra=palabra[1:-1]
            palindromo(palabra)
            return True

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           