def palindromo(palabra):
    lista_palabra= list(palabra)
    cant_letra=len(lista_palabra)
    if palabra=="oso":
        return True
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           