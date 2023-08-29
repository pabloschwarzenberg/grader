#CÓDIGO RECURSIVO
def palindromo(palabra):
    lista_palabra = list(palabra)
    if len(list(palabra)) <= 1:
        return(True)
    elif lista_palabra[0] == lista_palabra[len(lista_palabra)-1]:
        lista_palabra.pop(0)
        lista_palabra.pop(len(lista_palabra)-1)
        palabra = "".join(lista_palabra)
        #print(palabra)
        return(palindromo(palabra))
    elif len(list(palabra)) > 1:
        return(False)

#CÓDIGO NO RECURSIVO:
#def palindromo(palabra):
    #lista_palabra = list(palabra)
    #while (lista_palabra[0] == lista_palabra[len(lista_palabra)-1]) and len(lista_palabra) > 1:
        #print(lista_palabra)
        #lista_palabra.pop(0)
        #lista_palabra.pop(len(lista_palabra)-1)
        #return(True)
    #return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           