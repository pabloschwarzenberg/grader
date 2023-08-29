def palindromo(palabra):
    largo=len(palabra)
    if largo==1 or largo==0:
        return True
    
    if palabra[0]==palabra[largo-1]:
        palabra=palabra.replace(palabra[0],"")
        print(palabra)    
        palindromo(palabra)
        if palindromo:
            return True
    if palabra[0]!=palabra[largo-1]:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

