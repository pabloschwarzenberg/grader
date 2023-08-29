def jerigonzo(string):
    vocales=["a","e","o","u","i"]
    palabra=""
   
    
    for i in string:
        if i in vocales:
            palabra+=i
            palabra+="p"
        palabra+=i
    
    
        
    return palabra