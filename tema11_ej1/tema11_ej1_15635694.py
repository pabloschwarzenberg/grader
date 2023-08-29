def palindromo(palabra):
    l=len(palabra)-1
    if l<=0:
        return True
    else:
        if palabra[0]==palabra[l]:
            return palindromo(palabra[1:l])
        else:
            return False
        
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
    print(palindromo("winniw"))
           
