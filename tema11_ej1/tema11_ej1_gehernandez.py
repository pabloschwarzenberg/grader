def palindromo(palabra):
    p=len(palabra)
    if p>=4:
        if palabra[0]==palabra[(p-1)]:
            palabra=palabra.strip(palabra[(p-1)])
            palabra=palabra.strip(palabra[0])
            return palindromo(palabra)
        else:
            return False
    elif palabra[0]==palabra[2]:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           