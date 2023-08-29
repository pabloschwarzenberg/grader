def jerigonzo(string):
    lista_string = []
    vowels = 'aeiou'
    for i in range(len(string)):
        if string[i] in vowels:
            lista_string.append(string[i] + 'p' + string[i])
            print(lista_string)
        else:
            lista_string.append(string[i])

    string = "".join(lista_string)
    return string


if __name__ == "__main__":
    string = input('Por favor ingrese la cadena: ')
    print(jerigonzo(string))
