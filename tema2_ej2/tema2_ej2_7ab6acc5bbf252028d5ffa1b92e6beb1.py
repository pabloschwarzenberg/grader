def amigos(a,b):
    i=a
    p=b
    A=0
    B=0
    while i>1:
        if a%i==0:
            c=a/i
            A=A+c
        i=i-1
    while p>1:
        if b%p==0:
            d=b/p
            B=B+d
        p=p-1
    if A==b and B==a:
        return True
    else:
        return False
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
print(amigos(a,b))