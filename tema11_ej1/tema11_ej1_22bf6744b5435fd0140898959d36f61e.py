def palindromo(palabra):

    if len(palabra)==0:
        return True
        
    elif len(palabra)%2==1:
        pos=len(palabra)//2
        palabra=list(palabra)
        palabra.pop(pos)
        return palindromo(palabra)
    
    else:
        if palabra[0]==palabra[-1]:
            palabra=list(palabra)
            palabra.pop(0)
            palabra.pop(-1)
            return palindromo(palabra)
        
        else:
            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           