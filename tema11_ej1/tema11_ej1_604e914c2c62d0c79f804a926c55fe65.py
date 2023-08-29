def palindromo(palabra):
    if len(palabra)==1:
        return True
    elif palabra[0]==palabra[(len(palabra)-1)]:
        palabra=palabra[1:len(palabra)-1]
        if palindromo(palabra):
            return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))