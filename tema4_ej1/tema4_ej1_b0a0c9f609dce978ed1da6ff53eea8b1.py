from random import randint
def ocultar_letras(palabra,cantidad):
    new_palabra = palabra
    for x in range(0,cantidad):
        p = randint(0, len(palabra)-1)
        arr_p = list(new_palabra)
        arr_p[p] = '_'
        new_palabra = arr_p
    print("".join(arr_p))
    ret_paralabra = "".join(new_palabra)
    return ret_paralabra

def revisar_letra(palabra_secreta,palabra,letra):
    return_palabra = palabra
    if letra in palabra_secreta:
        print('is in')
        for index in range(0, len(palabra_secreta)):
            print(palabra_secreta[index])
            print(palabra[index])
            if palabra_secreta[index] != palabra[index] and palabra_secreta[index] == letra:
                print(letra)
                list_palabra = list(palabra)
                list_palabra[index] = letra
                return_palabra = "".join(list_palabra)
                print(return_palabra)
    return return_palabra