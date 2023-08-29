def amigos(a, b):
    suma_a = 0
    suma_b = 0
    for i in range(1, a):
        if a % i == 0:
            suma_a += i

    for k in range(1, b):
        if b % k == 0:
            suma_b += k

    return suma_a == b and suma_b == a

    # Cuerpo del programa


 n_1 = int(input('Introduzca el numero 1: '))
 n_2 = int(input('Introduzca el numero 2: '))

if amigos(n_1, n_2):
    print('¡Son amigos! :)')
else:
    print('No son amigos :(')
