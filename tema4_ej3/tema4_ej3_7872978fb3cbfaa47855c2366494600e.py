def jerigonzo(string):
    vocales = ['a','á','e','é','i','í','o','ó','u','ú']
    i = 0
    while i < len(vocales):
        r = vocales[i]+'p'+vocales[i]
        string = string.replace(vocales[i],r,len(string))
        i = i + 1
    return string
    
    
         