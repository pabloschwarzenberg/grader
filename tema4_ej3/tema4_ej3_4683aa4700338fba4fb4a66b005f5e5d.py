def jerigonzo(palabra):

    vocales = ['a', 'e', 'i', 'o', 'u']

    copia = ''
    for letra in palabra:
        copia = copia + letra

        if letra in vocales:
            copia = copia + 'p' + letra 
        
    return copia
    
         