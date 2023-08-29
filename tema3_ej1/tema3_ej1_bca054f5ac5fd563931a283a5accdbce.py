
def suma_divisores(num):
    div = []
    sum = 0
    for i in range(1, num - 1):
        if (num % i) == 0:
            div.append(i)
    for j in div:
        sum += j
    if sum == 1:
        return sum, True
    else:
        return sum, False