def palindromo(palabra):
    palabra_1=palabra
    lista=[]
    for i in palabra:
        lista.append(i)
    lista.reverse()
    palabra_2="".join(lista)
    if palabra_2==palabra_1:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           