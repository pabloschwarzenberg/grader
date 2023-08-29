# completa el código de la función
def amigos(a,b):
    totalA=0
    totalB=0

    for num in range(1,a-1):
        if a%num == 0:
            totalA+=num
    if totalA==b:
        for num in range(1,b-1):
            if b%num == 0:
                totalB+=num
        if totalB==a:
            return True

    return False
print(amigos(6,10))
           