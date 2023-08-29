def jerigonzo(string):
    palabra = ''
    x = 0
    while x < len(string):
        if string[x] == 'a' or string[x] == 'i' or string[x] == 'u' or string[x] == 'e' or string[x] == 'o':
            palabra = palabra+string[x]+'p'+string[x]
        else:
            palabra = palabra+string[x]
        x += 1
    return palabra