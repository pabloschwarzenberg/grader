def palindromo(a):
    b=list(a)
    a=list(a)
    a.reverse()
    global lista
    for i in range(len(a)):
        if a[i] == b[i]:
            a.insert(a.index(a[i]),1)
            a.pop(a.index(a[i]))
            lista.append(0)
        else:
            lista.append(1)
    if lista.count(0)== len(lista):
        return True
    else:
        return False
 
lista=[]
if __name__=="__main__":
    a=str(input('Ingrese:'))
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))