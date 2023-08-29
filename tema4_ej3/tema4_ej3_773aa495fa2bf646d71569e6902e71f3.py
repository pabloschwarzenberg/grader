# Jerigonzo
# 3 points
#
# Crea una función, que reciba un texto, y retorne el mismo texto traducido a jerigonzo.
# El Jerigonzo, es un idioma en que después de cada vocal, se agrega una p, y repite la vocal.

# Al codificar la frase 'estamos programando' tu funcion debiera retornar epestapamopos propograpamapandopo

vocals = ['a','e','i','o','u']

def jerigonzo(string):
    phrase = ''
    for l in string:
        if l in vocals:
            phrase = phrase + l + 'p' + l
        else:
            phrase = phrase + l
    return phrase
