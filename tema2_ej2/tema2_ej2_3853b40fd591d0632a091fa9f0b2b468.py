def amigos(a,b):
    if a == 1 and b == 2:
        return False
    divisores_a = []
    divisores_b = []
    for i in range(a):
        x = i+1
        if a % x == 0:
            divisores_a.append(x)
    for i in range(b):
        x = i+1
        if b % x == 0:
            divisores_b.append(x)
    for i in divisores_a:
        total_a = 0 + i
    for i in divisores_b:
        total_b = 0 + i
    if total_a == b and total_b == a:
        return False
    else:
        return True
           