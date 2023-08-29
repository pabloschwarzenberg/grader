"""
11.- Dos números a y b se dicen números amigos, si la suma de los divisores de uno
de los números es igual al otro número y viceversa (en el cálculo de los divisores, no debes
considerar al mismo número). Crea una función que reciba 2 números, y retorne True si es que
estos son amigos, y False si es que no lo son.
"""

def numeros_amigos(a, b):
    a = int(a)
    b = int(b)
    respuesta1 = False
    suma1 = 0
    for n in range(1, a):
        if (a%n) == 0:
            suma1 += n
    if suma1 == b:
        respuesta1 = True

    respuesta2 = False
    suma2 = 0
    for n in range(1, b):
        if (b%n) == 0:
            suma2 += n
    if suma2 == a:
        respuesta2 = True
    
    if respuesta
   1 and respuesta2:
        return True
    else:
        return False

a, b = map(int, input("a, b: ").split())

resultado = numeros_amigos(a, b)
print(resultado)