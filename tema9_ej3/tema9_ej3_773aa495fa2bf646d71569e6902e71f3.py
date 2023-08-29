# Decodificador
# 3 points
#
# Los computadores representan toda la información usando números, incluso las letras de las palabras.
# Para hacerlo, se utiliza el código ASCII, que asocia un número a cada letra o símbolo.
# Escribe una función llamada decodificar que debe recibir como parámetro un mensaje como
# string y retornar el mensaje descifrado usando las siguientes reglas:
#
# - El mensaje es una secuencia de números binarios de 8 dígitos separados por comas.
# Debes convertir cada número binario a su equivalente decimal.
# - Luego debes convertir cada número en la letra o símbolo que representa, usando la función chr.
# (para convertir una letra en su código ASCII asociados puedes usar ord).
# - Una vez que tengas todas las letras debes unirlas y retornarlas como el resultado de la función.
#
# Al decodificar 01101000,01101111,01101100,01100001 el resultado debiera ser hola

def decodificar(m):
    binary_values = m.split(',')
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string
