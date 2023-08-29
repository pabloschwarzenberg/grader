# completa el código de la función
def amigos(a, b):
        suma_a = 0
        suma_b = 0
        for i in range(1, a):
            if a % i == 0:
                suma_a += i
                print('a',suma_a)
        for k in range(1, b):
            if b % k == 0:
                suma_b += k
                print('b',suma_b)
        if suma_a != b and suma_b != a or a==1 or b==1:
            return False
        if  suma_a == b and suma_b == a:
            return True