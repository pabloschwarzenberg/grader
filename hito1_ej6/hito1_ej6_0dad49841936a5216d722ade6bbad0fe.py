#Ordenar tres números
a = int(input("ingrese primer numero: "))
b = int(input("ingrese segundo numero: "))
c = int(input("ingrese tercer numero: "))

if a >= b >= c:
    print(str(c)+","+str(b)+","+str(a))
elif b >= c >= a:
    print(str(a)+","+str(c)+","+str(b))
elif c >= a >= b:
    print(str(b)+","+str(a)+","+str(c))

elif a <= b <= c:
    print(str(a)+","+str(b)+","+str(c))
elif b <= c <= a:
    print(str(b)+","+str(c)+","+str(a))
elif c <= a <= b:
    print(str(c)+","+str(a)+","+str(b))