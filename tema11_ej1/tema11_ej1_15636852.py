def palindromo(palabra):
    lista=list(palabra)
    l=len(lista)

    if lista[0]==lista[l-1]:
        lista.pop(l-1)
        if l==1:
            return palindromo("".join(lista))
        else:
            return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))