def palindromo(palabra):
    i=0
    l=len(palabra)-1
    while i<=1:
        if palabra[i]!=palabra[l-i]:
            return False
        i=i+1
    return True
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           