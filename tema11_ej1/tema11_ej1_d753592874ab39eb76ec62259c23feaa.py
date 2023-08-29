def palindromo(palabra):
    palabra_3=palabra
    palabra=list(palabra)
    palabra_2=""
    if len(palabra)==1 or len(palabra)==0:
        return True
    else:
        if palabra[0]==palabra[::-1][0]:
            palabra_2=palabra[1:(len(palabra)-1)]
            return palindromo(palabra_2)
        else:
            return False


        

        

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))