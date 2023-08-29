def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']
    string = list(string)
    string_new = ""
    i = 0
    while i < len(string):
        if string[i] in vocales:
            string[i] = (string[i] + 'p' + string[i])
            i += 1
        else:
            i += 1
    for a in string:
        if a != ' ':
            string_new += a
        else:
            string_new += ' '


    return string_new

print(jerigonzo('estamos programando'))

if __name__ == "__main__":
    pass
         