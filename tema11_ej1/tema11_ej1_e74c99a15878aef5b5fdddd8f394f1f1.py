def palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:
        return True
    palabra=list(palabra)
    primera=palabra.pop(0)
    ultima=palabra.pop()
    if primera==ultima:
        return palindromo("".join(palabra))
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))