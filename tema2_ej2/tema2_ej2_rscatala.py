# completa el código de la función
def amigos(n1,n2):
    sum_divisores_n1 = 0
    i=1
    while i < n1:
        if n1%i == 0:
            sum_divisores_n1 += i
        i = i+1
    sum_divisores_n2 = 0
    j = 1
    while j < n2:
        if n2%j == 0:
            sum_divisores_n2 += j
        j = j+1
    if sum_divisores_n1 == n2 and sum_divisores_n2 == n1:
        return True
    else:
        return False
           