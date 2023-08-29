def jerigonzo(string):
    vocales='AaEeIiOoUu'
    for i in vocales:
        if i in vocales:
            string=string.replace(i,i+'p'+i)
    return string