def palindromo(palabra):
    palabra=list(palabra)
    if len(palabra)==1:
        return True
    elif len(palabra)==2:
        if palabra[0]==palabra[1]:
             return True
        else:
             return False
    elif len(palabra)==3:
        if palabra[0]==palabra[2]:
             return True
        else:
             return False
    else:
        while True:
            if palabra[0]==palabra[-1]:
                palabra.remove(palabra[0])
                palabra.remove(palabra[-1])
                palindromo(palabra)
            else:
                return False
             
    
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           