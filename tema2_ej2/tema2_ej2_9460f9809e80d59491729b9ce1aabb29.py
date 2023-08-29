def amigos(a, b):
    sum_a = sum(divisores(a))
    sum_b = sum(divisores(b))
    return sum_a == b and sum_b == a

def divisores(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
    return divs