import copy
def palindromo(palabra):
    lista=list(palabra)
    lista2=copy.copy(lista)
    lista2.reverse()
    print(lista)
    print(lista2)

    for i in range (len(palabra)):
        if lista[i]==lista2[i]:
            return True
        else:
            return False
         

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))