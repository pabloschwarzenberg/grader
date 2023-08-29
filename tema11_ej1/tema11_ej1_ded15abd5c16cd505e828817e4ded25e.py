def palindromo(palabra):
    palabra=list(palabra)
    a=palabra[0]
    b=palabra[len(palabra)-1]
    if len(palabra)==1:
        return True
    if a==b:
        palabra.remove(a)
        palabra.remove(b)
        return palindromo(palabra)
    if a!=b:
        return False
    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
    

           