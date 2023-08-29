def jerigonzo(string):
    vocales = 'aeiou'
    jeri=''
    c=-1
    while ''!=string:
        c+=1
        if string[c] in vocales:
            silaba = string[:c+1] + 'p' + string[c]
            jeri += silaba
            string = string[c+1:]
            c=-1
    string = jeri
    return string

         