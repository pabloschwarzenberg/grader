def palindromo(palabra):
    if len(palabra)==1:
         return True
    elif len(palabra)>=2 and palabra[0]==palabra[-1]:
        if palindromo(palabra[1:len(palabra)-1])==True:
            return True
        else:
            return False
    else:
        return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           