def son_amigos(a, b):
    sum_div_a = sum([x for x in range(1, a) if a % x == 0])
    sum_div_b = sum([x for x in range(1, b) if b % x == 0])
    return sum_div_a == b and sum_div_b == a
