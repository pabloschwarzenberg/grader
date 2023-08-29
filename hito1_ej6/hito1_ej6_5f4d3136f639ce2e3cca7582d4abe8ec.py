#Ordenar tres números
a=int(input("digite un numero entero"))
b=int(input("digite un segundo numero entero"))
c=int(input("digite un tercer numero entero"))
if(a<=b<=c):
    print("orden de menor a mayor", [a,b,c])
elif(a<=c<=b):
    print("orden de menor a mayor", [a,c,b])
elif(b<=c<=a):
    print("orden de menor a mayor", [b,c,a])
elif (b <= a <= c):
    print("orden de menor a mayor", [b, a, c])
elif (c <= b <= a):
    print("orden de menor a mayor", [c, b, a])
elif(c<=a<=b):
    print("orden de menor a mayor", [c,a,b])