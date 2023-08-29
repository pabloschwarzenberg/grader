# completa el código de la función
def amigos(a, b):
    return sum(divisor for divisor in range(1, a) if a % divisor == 0) == b and sum(divisor for divisor in range(1, b) if b % divisor == 0) == a
