def amigos(a,b):
    divisores_a=[0]
    divisores_b=[0]
    for i in range(1,a):
        if a%i==0:
            divisores_a.append(i)
    for i in range(1,b):
        if b%i==0:
            divisores_b.append(i)
    x = sum(divisores_a)
    y = sum(divisores_b)
    if x==b and y==a:
        return(True)
    else:
        return(False)
r=amigos(284,220)
print(r)