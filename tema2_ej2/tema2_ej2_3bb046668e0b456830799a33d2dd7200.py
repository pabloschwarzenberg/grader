def amigos(a, b):
    sum_div_a = sum([i for i in range(1, a) if a % i == 0])
    sum_div_b = sum([i for i in range(1, b) if b % i == 0])
    
    return sum_div_a == b and sum_div_b == a
           