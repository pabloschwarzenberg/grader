def suma_divisores(a):
    divisores = [1]
    b=0

    for i in range(2, a + 1):
        if a % i ==0:
            divisores.append(i)
            b = sum(divisores)-a

    if b==0 or b>2 :
       b=False
    else:
       b=True

    return sum(divisores)-a,b