# Función buscarTodas
# 5 points
#
# Programa una función llamada buscarTodas(a,b), que encuentre todas las apariciones del
# string b en el string a, y retorne un string que representa a una secuencia de índices
# separada por espacios. Por ejemplo, al ejecutar buscarTodas(’tres tristes tigres’,’t’),
# debería retornar el string ’0 5 9 13’ (no hay espacios después del número 13).

# Al buscar t en 'tres tristes tigres' el resultado debiera ser 0 5 9 13

def buscarTodas(a,b):
    result = ''
    for l in range(len(a)):
        if b == a[l]:
            result = result + str(l) + ' '
    return result.strip()