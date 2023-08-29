def palindromo(palabra):
    palabra = list(palabra)
    if len(palabra)==1 or len(palabra)==0:
        return True
    elif len(palabra)!=0 or len(palabra)!=1:
        if palabra[0]==palabra[-1]:
            palabra.remove(palabra[0])
            palabra.remove(palabra[-1])
            palabra="".join(palabra)
            return palindromo(palabra)
        else:
            return False
    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           