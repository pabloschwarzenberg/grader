def amigos(a, b):
    es_amigo=bool()
    suma_a = 0
    suma_b = 0
    for i in range(1, a):
        if a % i == 0:
            suma_a += i

    for k in range(1, b):
        if b % k == 0:
            suma_b += k
    if suma_a==b and suma_b==a:
        es_amigo=True
        return es_amigo
    else:
        es_amigo=False
        return es_amigo