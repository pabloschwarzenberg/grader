def encontrar_divisores(a, b):
    divisores1 = []
    divisores2 = []

    for k in range(1, int(a)-1):
        if a % k == 0:
            divisores1.append(k)

    for j in range(1, int(b)-1):
        if b % j == 0:
            divisores2.append(j)
    
    div1 = sum(divisores1)
    div2 = sum(divisores2)

    if  div1 == div2:
        return True
    else:
        return False