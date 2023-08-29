def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0]!=palabra[len(palabra)-1]:
        return False
    else:
        return palindromo(palabra[1:len(palabra)-1])
   
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           