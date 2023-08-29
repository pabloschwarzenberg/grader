__author__ = 'Domingo'
def palindromo(palabra):
    lista=[]
    for letra in palabra:
        lista.append(letra)
    if len(lista)>1:
        if lista[0]==lista[-1]:
            lista.pop(0)
            lista.pop(-1)
            nueva_palabra=''.join(lista)
            return palindromo(nueva_palabra)
        else:
            return False
    else:
        return True


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))