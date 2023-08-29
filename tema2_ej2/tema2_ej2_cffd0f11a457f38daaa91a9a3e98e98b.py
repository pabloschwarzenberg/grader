def amigos(a,b):
    c = 0
    for i in range(1,a):
        if a % i == 0:
            c += i
    d = 0
    for j in range(1,b):
        if b % j == 0:
            d += j 
    if c==b and d==a:
        return True
    else:
        return False

    
a = int(input("Ingrese numero a: "))
b = int(input("Ingrese numero b: "))
print(amigos(a,b))