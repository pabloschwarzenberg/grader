print("a continuacion ingrese tres numeros enteros en cualquier orden")

a=int(input("primer numero: "))
b=int(input("segundo numero: "))
c=int(input("tercer numero: "))

if a <= b <= c:
    print(a,",",b,",",c)

elif a <= c <= b:
    print(a,",",c,",",b)

elif b <= c <= a:
    print(b,",",c,",",a)

elif b <= a <= c:
    print(b,",",a,",",c)

elif c <= a <= b:
    print(c,",",a,",",b)

elif c <= b <= a:
    print(c,",",b,",",a)
