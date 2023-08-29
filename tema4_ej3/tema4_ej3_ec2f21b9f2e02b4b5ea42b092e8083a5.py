def jerigonzo(string):
    lista=["a","e","i","o","u"]

    palabra=""
    a=0
    for x in string:
        if x in lista:
           
            palabra=palabra+x+"p"+x

        else:

            palabra = palabra + string[a]

            
        a=a+1
    return palabra

        
