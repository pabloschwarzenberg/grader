#Ordenar tres números
a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
c=int(input("Ingrese c: "))
if a<=b and b<=c:
    print(a,b,c,sep=",")
elif a<=c and c<=b:
    print(a,c,b,sep=",")
elif b<=a and a<=c:
    print(b,a,c,sep=",")
elif b<=c and c<=a:
    print(b,c,a,sep=",")
elif c<=a and a<=b:
    print(c,a,b,sep=",")
else:
    print(c,b,a,sep=",")