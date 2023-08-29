def jerigonzo(string):
    jeri = ''
    vocales = 'AEIOUaeiou'
    for caracter in string:
        jeri += caracter
        if caracter in vocales:
            jeri += 'p' + caracter.lower()
    string = jeri
    return string

if __name__ == "__main__":
    pass
         