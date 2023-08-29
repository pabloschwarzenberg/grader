def palindromo(palabra):
    if palabra[0] != palabra[len(palabra)-1]:
        return False
    elif len(palabra)<=2:
        return True
    else:
        return palindromo(palabra[1:len(palabra)-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           