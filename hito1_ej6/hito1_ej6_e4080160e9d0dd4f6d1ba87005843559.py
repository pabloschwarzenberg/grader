#Ordenar tres números
a = int(input("Ingrese el Primer  número: "))
b = int(input("Ingrese el Segundo  número: "))
c = int(input("Ingrese el Tercer  número: "))
if a <= b <= c:
    print ("Los números ordenados son",(a, b, c))
elif a <= c <= b:
    print ("Los números ordenados son",(a, c, b))
elif b <= a <= c:
    print ("Los números ordenados son",(b, a ,c))
elif b <= c <= a:
    print ("Los números ordenados son",(b, c ,a))
elif c <= a <= b:
    print ("Los números ordenados son",(c, a ,b))
elif c <= b <= a:
    print ("Los números ordenados son",(c, b, a))