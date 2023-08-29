def palindromo(palabra):
    palabra.split()
    if len(palabra)<=1:
        return True
    else:
        if palabra[0]==palabra[-1]:
            lista=list(palabra)
            lista[0]=""
            lista[-1]=""
            palabra="".join(lista)
            return palindromo(palabra)
        else:
            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           