def palindromo(palabra):
    if len(palabra)==0 or len(palabra)==1:
        return True
    if palabra[0]==palabra[-1]:
        return palindromo(palabra[1:len(palabra)-1])
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           