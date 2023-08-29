def palindromo(palabra):
    palabra=str(palabra)
    f=len(palabra)
    if len(palabra)==1 or len(palabra)==0:
        return True
    if palabra[0]==palabra[-1]:
        if f==3:
            return True
        else:
            palabra=palabra[1:f-1]
            palindromo(palabra)
    else:
        return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
 


           