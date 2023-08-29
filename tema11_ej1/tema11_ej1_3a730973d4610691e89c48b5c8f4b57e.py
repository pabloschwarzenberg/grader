def palindromo(palabra):
    if len(palabra)==1:
        return True
    if len(palabra)==2:
        a=palabra[0]
        b=palabra[1]
        if a==b:
            return True
        else:
            return False
    else:
        a=palabra[0]
        b=palabra[len(palabra)-1]
        if a==b:
            palabra=palabra[1:-1]
            return palindromo(palabra)
        else:
            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           