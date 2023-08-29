def jerigonzo(string):
        p="p"
        newString=""
        for j in string:
            if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
                newString=newString + j+p+j
            else:    
                newString=newString + j
                
        return(newString)
