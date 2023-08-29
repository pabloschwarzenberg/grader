# completa el código de la función
def amigos(a, b):
    sum_div_a = sum([num for num in range(1, a) if a % num == 0])
    sum_div_b = sum([num for num in range(1, b) if b % num == 0])
    
    return sum_div_a == b and sum_div_b == a
