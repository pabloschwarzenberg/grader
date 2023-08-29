def palindromo(palabra):
    nueva_palabra=""
    i=1

    if len(palabra)== 0 or len(palabra)== 1:
        return True
    else:
        if palabra[0] == palabra[len(palabra)-1]:
            while i<len(palabra)-1:
                nueva_palabra+=palabra[i]
                i+=1
                
            palindromo(nueva_palabra)
            if palindromo(nueva_palabra)==True:
                return True
        else:
            return False
        

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           