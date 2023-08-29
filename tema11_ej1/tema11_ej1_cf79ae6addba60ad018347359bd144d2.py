def palindromo(palabra,nuevo="",guardado=""):
    if guardado=="":
        guardado=palabra
    if len(palabra)!=0:
        nuevo=nuevo+palabra[len(palabra)-1]
    if len(palabra)==0:
        if nuevo == guardado:
            return True
        else:
            return False
    else:    
        return palindromo(palabra[:len(palabra)-1],nuevo,guardado)


      
        
    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           