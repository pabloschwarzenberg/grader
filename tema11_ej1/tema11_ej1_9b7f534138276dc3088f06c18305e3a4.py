def palindromo(palabra):
    palabra=list(palabra)
    reversa=[]
    for i in palabra:
        reversa.insert(0,i)
    if palabra==reversa:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           