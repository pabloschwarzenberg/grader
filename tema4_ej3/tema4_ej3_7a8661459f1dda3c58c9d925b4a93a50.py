
def jerigonzo(string):

    texto = ""

    for i in range(0,len(string)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            texto += string[i]
            texto += "p"
            texto += string[i]
        else:
            texto += string[i]
    return texto
if __name__ == "__main__":
    string = input('Ingrese un texto: ')
    print('Traduccion al jeringoso: ')
    print(jeringozo(string))
 