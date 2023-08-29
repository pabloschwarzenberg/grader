#Ordenar tres números
m1=int(input("introduzca el primer numero"))
m2=int(input("introduzca el segundo numero"))
m3=int(input("introduzca el tercer numero"))
a=min(m1,m2,m3)
c=max(m1,m2,m3)
b=(m1+m2+m3)-a-c
print("{},{},{}".format(a, b, c))      