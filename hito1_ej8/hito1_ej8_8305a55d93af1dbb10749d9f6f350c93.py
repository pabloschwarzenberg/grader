#Descomponer un número
n=int(input("ingrese su numero"))
x=n
d=n//1000
n=x%1000
e=n//100
n=x%100
f=n//10
n=x%10
g=n%10
if d>0:
      print((d),"M + ",(e),"C", "+ ",(f),"D + ",(g),"U")
elif d==0 and e>0:
    print((e),"C", "+ ",(f),"D + ",(g),"U")
elif d==0 and e==0 and f>0:
    print((f),"D + ",(g),"U")
elif d==0 and e==0 and f==0 and g>0:
    print((g),"U")
      