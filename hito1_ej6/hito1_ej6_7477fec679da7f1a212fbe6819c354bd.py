a=int(input("Ingrese un numero "))
b=int(input("Ingrese un numero "))
c=int(input("Ingrese un numero "))
if (a<=b and a<=c) and (b<=c):
    print((a),(b),(c))
elif (a<=b and a<=c) and (c<=b):
    print((a),(c),(b))
elif (b<=a and b<=c) and (a<=c):
    print((b),(a),(c))
elif (b<=a and b<=c) and (c<=a):
    print((b),(c),(a))
elif (c<=a and c<=b) and (a<=b):
    print((c),(a),(b))
elif (c<=a and c<=b) and (b<=a):
    print((c),(b),(a))