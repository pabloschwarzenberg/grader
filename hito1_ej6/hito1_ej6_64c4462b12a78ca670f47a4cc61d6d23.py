#Ordenar tres números

a = int(input('N1: '))
b = int(input('N2: '))
c = int(input('N3: '))

if a <= b and b <= c:
    print(a, ',', b, ',', c)
elif c >= a and b >= c:
    print(a, ',', c, ',', b)
elif b <= c and c <= a:
    print(b, ',', c, ',', a)
elif b <= a and a <= c:
    print(b, ',', a, ',', c)
elif c <= a and a <= b:
    print(c, ',', a, ',', b)
elif c <= b and a <= a:
    print(c, ',', b, ',', a)
