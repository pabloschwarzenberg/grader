def palindromo(palabra):
    palabra=list(palabra)
    i=0
    j=len(palabra)-1
    if len(palabra)>3 and palabra[i]!=palabra[j]:
        return False
    else:
        if palabra[i]==palabra[j]:
            if len(palabra)==3:
                return True
            else:
                i+=1
                j-=1
                palindromo(palabra)

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           