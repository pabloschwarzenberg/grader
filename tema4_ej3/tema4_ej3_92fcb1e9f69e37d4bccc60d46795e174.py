def jerigonzo(string):
    palabra = ''
    v = ['a', 'e', 'i', 'o', 'u']
    for i in string:
        if i in v:
            palabra += i
            palabra += 'p'
            palabra += i
        else:
            palabra += i
    return palabra