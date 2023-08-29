def palindromo(palabra):
    c=len(palabra)
    if c==1 or c==0:
        return True
    if palabra[0] == palabra[c-1]:
        palabra=palabra[1:c-1]
        return palindromo(palabra)
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           