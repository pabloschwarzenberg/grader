def jerigonzo(string):
    palabra = ''
    for i in range(0, len(string)):
        if string[i] == 'a' or string[i] == 'o' or string[i] == 'e' or string[i] == 'i' or string[i] == 'u':
            palabra = palabra + string[i] + 'p' + string[i]
        else:
            palabra += string[i]
    return palabra

if __name__ == "__main__":
    pass
         