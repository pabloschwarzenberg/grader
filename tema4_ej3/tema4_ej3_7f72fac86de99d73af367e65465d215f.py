def jerigonzo(string):
    vocales="aeiouAEIOU"
    string=list(string)
    print(string)
    i=0
    while i<len(string):
        if string[i] in vocales:
            vocal=string[i]
            p="p"
            palabra=vocal+p+vocal
            string[i]=palabra
        i+=1
    cambio=""
    i=0
    while i<len(string):
        cambio=cambio+string[i]
        i+=1
    string=cambio
    return string