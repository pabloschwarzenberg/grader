def palindromo(palabra):
    lista=list(palabra)
    nueva_l=lista.copy()
    nueva_l.reverse()
    if lista==nueva_l:
        return True
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           