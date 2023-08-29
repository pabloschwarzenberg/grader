def jerigonzo(string):
    vocales= ["a", "e", "i" ,"o" , "u"]
    jerigonzo= []
    for letra in string:
        if letra in vocales:
            jerigonzo.append(letra)
            jerigonzo.append("p")
            jerigonzo.append(letra)
        else: jerigonzo.append(letra)
    traduccion= ""
    cont=0
    while cont<len(jerigonzo):
        traduccion= traduccion + str(jerigonzo[cont])
        cont= cont + 1
    return(traduccion)
         