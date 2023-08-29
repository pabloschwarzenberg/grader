def palindromo(palabra):
    ultimo=len(palabra)-1
    if len(palabra)==0 or len(palabra)==1:
        return True
    else:
        if palabra[0]==palabra[ultimo]:
            palabra=list(palabra)
            palabra.pop(0)
            palabra.pop()
            n_palabra="".join(palabra)
            return palindromo(n_palabra)
        if palabra[0]!=palabra[len(palabra)-1]:
            return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           