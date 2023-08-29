def divisores(num):
    div = []
    sum = 0
    for i in range(1, num - 1):
        if (num % i) == 0:
            div.append(i)
    for j in div:
        sum += j
    return sum

def numero_perfecto(num):
    sum = divisores(num)
    if num == sum:
        return True
    else:
        return False