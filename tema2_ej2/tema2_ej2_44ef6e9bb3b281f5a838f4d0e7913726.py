# completa el código de la función
def o(n):
    divisores = []
    for i in range( (n - 1), 0, -1):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)

def amigos(a, b):
    print( o(a) )
    print( o(b) )
    return o(a) == b and o(b) == a

# print(amigos(284, 220))
