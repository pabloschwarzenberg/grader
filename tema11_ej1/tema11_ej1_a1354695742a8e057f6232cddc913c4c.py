def palindromo(palabra):
    if len(palabra)==1:
        return True
    if len(palabra)==2:
        return(palabra[0]==palabra[1])
    else:
        cabeza=palabra[0]
        cuerpo=palabra[1:len(palabra)-1]
        cola=palabra[len(palabra)-1]
        cuerpo_p=palindromo(cuerpo)

        if cuerpo_p and (cabeza==cola):
            return True
        else:
            return False
  

    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           