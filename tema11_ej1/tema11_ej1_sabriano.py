def palindromo(palabra):
    lista=list(palabra)
    lista.reverse()
    l1="".join(lista)
    if l1==palabra:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           