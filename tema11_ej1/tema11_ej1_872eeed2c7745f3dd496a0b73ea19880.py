def palindromo(frase):
    l=len(frase)
    if l==1:
        return True
    frase1=frase[1:l-1]
    if(frase[0]==frase[l-1])and palindromo(frase1)==True:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           