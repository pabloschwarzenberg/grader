#Ordenar tres números
a=int(input("1.Ingrese un número: "))
b=int(input("2.Ingrese un número: "))
c=int(input("3.Ingrese un número: "))

if  a<=b<=c:
    print(str(a)+","+str(b)+","+str(c))
elif    a<=b>=c>=a:
    print(str(a)+","+str(c)+","+str(b))
elif    a<=b>=c<=a:
    print(str(c)+","+str(a)+","+str(b))
elif    a>=b<=c<=a:
    print(str(b)+","+str(c)+","+str(a))
elif    a>=b<=c>=a:
    print(str(b)+","+str(a)+","+str(c))
else    :
    print(str(c)+","+str(b)+","+str(a))