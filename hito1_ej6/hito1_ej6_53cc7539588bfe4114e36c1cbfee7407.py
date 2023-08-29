b=int(input("Inserte primer número "))
n=int(input("Inserte segundo número "))
m=int(input("Inserte tercer número "))
if b>n and b>m:
    if n>m:
        print(m,",",n,",",b)
    elif m>n:
        print(n,",",m,",",b)
elif n>b and n>m:
    if b>m:
        print(m,",",b,",",n)
    elif m>b:
        print(b,",",m,",",n)
elif m>b and m>n:
    if b>n:
        print(n,",",b,",",m)
    elif n>b:
        print(b,",",n,",",m)
elif b==n:
    if n<m:
        print(b,",",n,",",m)
    else:
        print(m,",",n,",",b)
elif b==m:
    if m<n:
        print(b,",",m,",",n)
    else:
        print(n,",",b,",",m)
elif m==n:
    if n<b:
        print(n,",",m,",",b)
    else:
        print(b,",",m,",",n)
elif b==n==m:
    print(b,",",n,",",m)