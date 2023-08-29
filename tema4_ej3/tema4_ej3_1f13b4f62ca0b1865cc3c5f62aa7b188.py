def jerigonzo(string):
    vocals = list('aeiou')

    for v in vocals: 
        p = string.split(v)
        if len(p) > 1: 
            jeri =v+ 'p' + v
        new_p = jeri.join(p)
        string = new_p
    
    return string
    
            


if __name__ == "__main__":

    palabra = input('Ingrese una palabra:\n ')
    print(
        'El equivalente en jerigonzo es:\n', jerigonzo(palabra)
    )
