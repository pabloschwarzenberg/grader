def palindromo(palabra):
    if len(palabra)==1:
        return palabra
    if palabra[0]==palabra[len(palabra)-1]:
        palindromo(palabra[1:len(palabra)-1])
    else:
        return False
    return True

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           