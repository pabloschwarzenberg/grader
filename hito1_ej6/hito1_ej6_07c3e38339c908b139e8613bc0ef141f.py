#Ordenar tres números
a=int(input("ingrese valor de a: "))
b=int(input("ingrese valor de b: "))
c=int(input("ingrese valor de c: "))

if (a<=b<=c):
    print(""+str(a)+", "+str(b)+", "+str(c)+"")

if (a<=c<=b):
    print(""+str(a)+", "+str(c)+", "+str(b)+"")

if (b<=a<=c):
    print(""+str(b)+", "+str(a)+", "+str(c)+"")

if (b<=c<=a):
    print(""+str(b)+", "+str(c)+", "+str(a)+"")

if (c<=a<=b):
    print(""+str(a)+", "+str(c)+", "+str(b)+"")

if (c<=b<=a):
    print(""+str(c)+", "+str(b)+", "+str(a)+"")