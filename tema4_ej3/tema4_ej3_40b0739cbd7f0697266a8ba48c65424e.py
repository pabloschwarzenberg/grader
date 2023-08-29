def jerigonzo(tex):
    lista = ''
    for letra in tex:
        if letra in 'AEIOUaeiou':   
            lista += letra
            lista += 'p'

        lista += letra

    print(lista)

    return lista    