#Aprobación de créditos
i = int(input())
e = int(input())
h = int(input())
ab = int(input())
ec = str(input())
v = str(input())
a = 'APROBADO'
r = 'RECHAZADO'
if ab > 10 and h >=2:
    print(a)
elif ec == 'C' and e >= 45 and e <=55:
    print(a)
elif i > 2500000 and ec == 'S' and v == 'U':
    print(a)
elif i > 3500000 and ab > 5:
    print(a)
elif v == 'R' and ec == 'C' and h < 2:
    print(a)
else:
    print(r)      