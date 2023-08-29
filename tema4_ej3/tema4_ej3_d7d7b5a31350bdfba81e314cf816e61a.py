def jerigonzo(string):
    palabra=string
    j=""
    vocales=["a","e","i","o","u"]
    for i in palabra:
        if i not in vocales:
            j+=i
        if i in vocales:
            j+=i
            j+="p"
            j+=i
    return j
         