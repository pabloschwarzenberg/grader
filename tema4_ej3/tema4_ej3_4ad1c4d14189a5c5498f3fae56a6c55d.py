print('** JERIGONZO **')
def jerigonzo(string):
    lista_vocal = ['a','e','i','o','u']
    lista_string = list(string)
    lista = []
    for i in lista_string:
        if i not in lista_vocal:
            lista.append(i)
        else:                       
            lista.append(i+'p'+i)
    string = ''.join(lista)
    return string

if __name__ == "__main__":
    string = input('Ingrese la palabra para traducirla: ')
    print(jerigonzo(string))