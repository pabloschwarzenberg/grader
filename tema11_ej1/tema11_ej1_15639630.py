
def palindromo(palabra):
    lista=[]
    if len(palabra)==1:
        return True

    for letra in palabra:
        lista.append(letra)

    if comparar(lista) == False:
        return False

    else:
        return palindromo(lista[1:len(lista)-1])


def comparar(lista):
    if lista[0] == lista[len(lista)-1]:
        return True
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           