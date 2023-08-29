def palindromo(palabra):
    if len(palabra)==0 or len(palabra)==1:
        return True
    else:
        if palabra[-1]==palabra[0]:
            palabra=palabra[1:len(palabra)-1]
            return palindromo(palabra)
        else:
            return False
            
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           