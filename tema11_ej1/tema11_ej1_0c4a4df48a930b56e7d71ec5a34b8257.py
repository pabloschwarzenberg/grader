def palindromo(palabra):
    lista=list(palabra)
    lista1=list(palabra)
    lista.reverse()
    if lista==lista1:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
