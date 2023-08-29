# completa el código de la función
def amigos(a,b):
    sum_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    sum_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    return sum_a == b and sum_b == a
           