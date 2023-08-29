#Sistema de Ecuaciones
def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  
 num=int(input("Ingrese Un numero: ")
 es_primo(num)
def numeros_amigos(x, y):
    sumax = 0
    sumay = 0
    for i in range(1, x):
        if x % i == 0:
            sumax += i

    for k in range(1, y):
        if y % k == 0:
            sumay += k

    if sumax == y and sumay == x:
        return True
    else:
        return False


n_1 = int(input('Introduzca el nº 1: '))
n_2 = int(input('Introduzca el nº 2: '))
numeros_amigos(n_1,n_2)      