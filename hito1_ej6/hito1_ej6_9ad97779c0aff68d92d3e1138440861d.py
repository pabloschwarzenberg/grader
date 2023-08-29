#Ordenar tres números
a=int(input("Escriba el primer numero"))
b=int(input("Escriba el segundo numero"))
c=int(input("Escriba el tercer numero"))

if a<=b<=c:
     m=print(a,b,c,sep=",")

if c<=b<=a:
    print(c,b,a,sep=",")

if a<=c<=b:
    print(a,c,b,sep=",")

if c<=a<=b:
    print(c,a,b,sep=",")

if b<=a<=c:
    print(b,a,c,sep=",")

if b<=c<=a:
    print(b,c,a,sep=",")
