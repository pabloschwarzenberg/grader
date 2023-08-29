def es_primo(x):
    divisor = 2
    while divisor < x:
        n = x % divisor
        if n == 0:
            divisor = x
        divisor = divisor + 1
    if divisor == x + 1:
        return False
    else:
        return True
res=es_primo(4)
print(res)