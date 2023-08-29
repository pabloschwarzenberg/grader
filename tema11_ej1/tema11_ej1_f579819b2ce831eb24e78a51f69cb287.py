def palindromo(palabra):
    palabra=list(palabra)
    if len(palabra)!=0:
        if palabra[0]==palabra[-1]:
            palabra.pop(0)
            if len(palabra)==0:
                return True
            else:
                palabra.pop(-1)
            if palindromo(palabra) == True:
                return True
            else:
                return False
        else:
            return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           