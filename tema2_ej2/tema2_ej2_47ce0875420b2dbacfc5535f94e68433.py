def amigos(a,b):
    i=1
    j=1
    divisores_a=0
    divisores_b=0
    while i<a:
        if a%i==0:
            print(i)
            divisores_a=divisores_a+i
            print(divisores_a)
        i=i+1
    while j<b:
        if b%j==0:
            print(j)
            divisores_b=divisores_b+j
            print(divisores_b)
        j=j+1
    if divisores_a==b and divisores_b==a:
        return True
    else:
        return False