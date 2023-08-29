# completa el código de la función
def amigos(a,b):
    sum_div_a = sum(divisores(a))
    sum_div_b = sum(divisores(b))
    return sum_div_a == b and sum_div_b == a

def divisores(n):
    return [i for i in range(1, n) if n % i == 0]           