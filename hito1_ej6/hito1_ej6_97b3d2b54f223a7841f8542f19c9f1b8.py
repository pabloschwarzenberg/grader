#Ordenar tres números
a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

if a>=b>=c:
    print("El orden es {},{},{}".format(c,b,a))
elif a>=c>=b:
        print("El orden es {},{},{}".format(b,c,a))

elif c>=a>=b:
        print("El orden es {},{},{}".format(b,a,c))

elif c>=b>=a:
        print("El orden es {},{},{}".format(a,b,c))

elif b>=a>=c:
    print("El orden es {},{},{}".format(c,a,b))
elif b>=c>=a:
        print("El orden es {},{},{}".format(a,c,b))