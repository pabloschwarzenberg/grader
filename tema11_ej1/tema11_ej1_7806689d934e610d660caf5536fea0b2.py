def palindromo(palabra):
    if palabra[0]!=palabra[len(palabra)-1]:
        return False
    else:
        return True
    return palidromo(palabra[1:len(palabra)-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
    print(palindromo("anana"))
    print(palindromo("menem"))
           