def jerigonzo(string):
        p="p"
        nuevoString=""
        for j in string:
            if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
                nuevoString=nuevoString + j+p+j
            else:    
                nuevoString=nuevoString + j
                
        return(nuevoString)

         