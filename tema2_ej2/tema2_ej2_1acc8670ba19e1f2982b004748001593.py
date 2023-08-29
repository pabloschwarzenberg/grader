# completa el código de la función
def amigos(a, b):
    if a == b:
        return False 
    sum_a = sum(e for e in range(1, a // 2 + 1) if a % e == 0)
    sum_b = sum(e for e in range(1, b // 2 + 1) if b % e == 0)
    return sum_a == b and sum_b == a
           