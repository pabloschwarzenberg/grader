#Descomponer un número
a=(input())
b=int(a)
if b>=1000:
    ac=(a[0])
    au=(a[1])
    ad=(a[2])
    at=(a[3])
    print(ac,"M+",au,"C+", ad,"D+",at,"U+")
elif b<=1000 and b>=100:
    ac=(a[0])
    au=(a[1])
    ad=(a[2])
    print(ac,"C+",au,"D+", ad,"U")
elif b<=100 and b<=100 and b>=10:
    ac=(a[0])
    au=(a[1])
    print(ac,"D+",au,"U")
elif b<=1000 and b<=100 and b<=10:
    ac=(a[0])
    print(ac,"U")