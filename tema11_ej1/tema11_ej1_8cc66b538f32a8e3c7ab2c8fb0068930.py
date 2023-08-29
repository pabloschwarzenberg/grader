def palindromo(palabra):
    lista=[]
    n=len(palabra)-1
    while n>=0:
        lista.append(palabra[n])
        n=n-1
    palabra1="".join(lista)
    if palabra==palabra1:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           
