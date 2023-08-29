#Ordenar tres números
a=int(input("primer número entero:"))
b=int(input("segundo número entero:"))
c=int(input("tercer número entero:"))
if a<=b<=c:
    orden1 = a,b,c
    print("el orden de menor a mayor es:",orden1)
elif a<=c<=b:
    orden2 = a,c,b
    print("el orden de menor a mayor es:",orden2)
elif b<=a<=c:
    orden3 = b,a,c
    print("el orden de menor a mayor es:",orden3)
elif b<=c<=a:
    orden4 = b,c,a
    print("el orden de menor a mayor es:",orden4)
elif c<=a<=b:
    orden5 = c,a,b
    print("el orden de menor a mayor es:",orden5)
elif c<=b<=a:
    orden6 = c,b,a
    print("el orden de menor a mayor es:",orden6)
else:
    print("los valores son iguales")

         