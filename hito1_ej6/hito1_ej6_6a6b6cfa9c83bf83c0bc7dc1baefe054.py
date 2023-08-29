a=int(input("Escriba el primer numero "))
b=int(input("Escriba el segundo numero "))
c=int(input("Escriba el tercer numero "))
if a<b<c:
    print(a,b,c)

elif c<=b<=a:
    print(c,b,a)
elif b<=c<=a:
    print(b,c,a)
elif b<=a<=c:
    print(b,a,c)
elif c<=a<=b:
    print(c,a,b)
elif c<=b<=a:
    print(c,b,a)
