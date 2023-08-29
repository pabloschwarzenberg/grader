#Ordenar tres números
#entrada:entregeme 3 numeros
#salida:mostrarme los numeros de menor a mayor
#1.numero 1
n1=int(input("numero 1: "))
#2.numero 2
n2=int(input("numero 2: "))
#3.numero 3
n3=int(input("numero 3: "))
#4.ordenar los numeros de menor a mayor
if n1<=n2<=n3:
    print(n1,",",n2,",",n3)
elif n2<=n1<=n3:
    print(n2,",",n1,",",n3)
elif n3<=n2<=n1:
    print(n3,",",n2,",",n1)
elif n1<=n3<=n2:
    print(n1,",",n3,",",n2)
elif n2<=n3<=n1:
    print(n2,",",n3,",",n1)
elif n3<=n1<=n2:
    print(n3,",",n1,",",n2)
