def amigos(a, b):
    if a == b:
        return False

    def sum_divisores(n):
        return sum([i for i in range(1, n) if n % i == 0])

    sum_div_a = sum_divisores(a)
    sum_div_b = sum_divisores(b)

    return sum_div_a == b and sum_div_b == a
