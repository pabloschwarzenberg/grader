# Encriptador ROT13
# 3 points
#
# El encriptador ROT13, es un tipo de cifrado llamado de desplazamiento.
# Este tipo de cifrados eran usados en tiempos de los romanos para proteger mensajes militares importantes.
# Se dice que Julio César, usaba este tipo de algoritmo para proteger sus mensajes, razón por la cual,
# se le suele llamar “cifrado César” a este tipo de codificación. Crea la función rot13 que reciba una
# palabra y la retorne encriptada.

# Al encriptar hola el resultado debiera ser ubyn
# Al encriptar camioneta el resultado debiera ser pnzvbargn
# Al encriptar zorro el resultado debiera ser mbeeb

def rot13(word):
    x = 'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz'
    y = 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm'
    table = word.maketrans(x, y)
    return word.translate(table)           