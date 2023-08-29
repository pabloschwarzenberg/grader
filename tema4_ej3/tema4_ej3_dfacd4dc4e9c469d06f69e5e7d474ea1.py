def jerigonzo(string):
    trad = []
    string = list(string)
    vocales = ['a','e','i','o','u']
    for i in string:
        if i in vocales:
            trad += i + 'p' + i
        else:
            trad += i

    trad = ''.join(trad)
    return trad

if __name__ == "__main__":
    pass
         