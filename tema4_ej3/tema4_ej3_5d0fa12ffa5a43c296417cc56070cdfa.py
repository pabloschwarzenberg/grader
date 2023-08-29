def jerigonzo(string):
    vocales = 'aeiou'
    nueva = ''

    for i in string:
        if str(i) in vocales:
            nueva = nueva + str(i)+ 'p'+ str(i)
        else:
            nueva = nueva+str(i)

    return nueva


         