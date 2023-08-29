#Ordenar tres números
a=int(input("ingrese un número: "))
b=int(input("ingrese un número: "))
c=int(input("ingrese un número: "))

if a<b and b<c:
            print(str(a) + "," + str(b) + "," + str(c))
elif a<c and c<b:
            print(str(a) + "," + str(c) + "," + str(b))
elif b<a and a<c:
            print(str(b) + "," + str(a) + "," + str(c))
elif b<c and c<a:
            print(str(b) + "," + str(c) + "," + str(a))
elif c<b and b<a:
            print(str(c) + "," + str(b) + "," + str(a))
elif c<a and a<b:
            print(str(c) + "," + str(a) + "," + str(b))
elif a==b and a<c:
    print(str(a) + "," + str(b) + "," + str(c))
elif a==c and a<b:
    print(str(a) + "," + str(c) + "," + str(b))
elif a==b and c<a:
    print(str(c) + "," + str(a) + "," + str(b))
elif a==c and b<a:
    print(str(b) + "," + str(a) + "," + str(c))
elif b==c and a<b:
    print(str(a) + "," + str(b) + "," + str(c))
elif b==c and b<a:
    print(str(b) + "," + str(c) + "," + str(a))
