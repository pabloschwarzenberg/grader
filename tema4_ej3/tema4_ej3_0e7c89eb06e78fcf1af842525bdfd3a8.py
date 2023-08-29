def jerigonzo(string):

    temp = []
    vocales = ['a', 'e', 'i', 'o', 'u']
    for x in string:
        temp.append(x)
        if x in vocales:
            temp.append('p')
            temp.append(x)
            
    string = "".join(temp)
    return string

if __name__ == "__main__":
    print(jerigonzo("hola"))