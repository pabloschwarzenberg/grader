def jerigonzo(string):
    lista=["a","e","i","o","u"]

    palabra=""
    cont=0
    for x in string:
        if x in lista:
           
            palabra=palabra+x+"p"+x

        else:

            palabra = palabra + string[cont]

            
        cont=cont+1
    return palabra

      