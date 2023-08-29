def palindromo(palabra):
    palabra=list(palabra)
    if len(palabra)==1 or len(palabra)==0:
        return True
    
    elif len(palabra)%2!=0:
        for i in range(int((len(palabra)-1)/2)):
            if palabra[0]==palabra[-1]:
                palabra.pop()
                palabra.pop(0)
                
                return palindromo(palabra)
            else:
                return False

    elif (len(palabra)%2)==0:
        
        for i in range(int((len(palabra)/2))):
            if palabra[0]==palabra[-1]:
                palabra.pop()
                palabra.pop(0)
                return palindromo(palabra)
            else:
                return False
        
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           