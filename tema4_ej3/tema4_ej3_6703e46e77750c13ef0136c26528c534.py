def jerigonzo(string):
    string = list(string)
    vocales = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(string)):
        if string[i] in vocales:
            string[i] += 'p' + string[i]
    
    return ''.join(string)

jerigonzo("paralelepipedo")