def palindromo(palabra):
    lista=[]
    for i in palabra:
        lista.append(i)
    lista_inversa=lista[::-1]
    if lista==lista_inversa:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           