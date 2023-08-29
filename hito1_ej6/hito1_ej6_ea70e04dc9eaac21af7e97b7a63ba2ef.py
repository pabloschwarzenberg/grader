a=int(input("digite el primer numero entero"))
b=int(input("digite el segundo numero entero"))
c=int(input("digite el tercero numero entero"))
a1=min(a,b,c)
b2=max(a,b,c)
c3=(a+b+c)-a1-b2
print(a1,",",c3,",",b2)