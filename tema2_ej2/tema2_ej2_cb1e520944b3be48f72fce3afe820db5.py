def amigos (a,b):
    sum_a = 0
    sum_b = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a = (sum_a) + i
    for i in range(1, b):
        if b % i == 0:
            sum_b = (sum_b) + i
    if sum_a==b and sum_b==a:
        amigos=True
    else:
        amigos=False
    return amigos
