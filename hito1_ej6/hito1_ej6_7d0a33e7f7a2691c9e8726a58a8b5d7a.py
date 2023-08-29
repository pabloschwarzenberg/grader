#Ordenar tres números
n1 = float(input("introduzca el primer numero:"))
n2 = float(input("introduzca el segundo numero:"))
n3 = float(input("introduzca el tercer numero:"))

if n1 < n2 < n3:
    print(n1,",",n2,",",n3)
if n3<n2<n1:
    print(n3,",",n2,",",n1)
if n2<n1<n3 :
    print(n2,",",n1,",",n3)
if n2<n3<n1:
    print(n2,",",n3,",",n1)
if n1 < n3 < n2:
    print(n1,",",n3,",",n2)
if n3 < n1 < n2:
    print(n3,",",n1,",",n2)
    