#Ordenar tres números
a=input("Ingrese un número: ")
b=input("Ingrese un número: ")
c=input("Ingrese un número: ")

if ((a<b and b<c) or (a<b and b==c)) :
    print("El orden de los números de menor a mayor es: ",a,",",b,",",c)
if ((c<b and b<a) or (c<b and b==a)) :
    print("El orden de los números de menor a mayor es: ",c,",",b,",",a)
if ((a<c and c<b) or (a==c and c<b)) :
    print("El orden de los números de menor a mayor es: ",a,",",c,",",b)
if ((b<c and c<a) or (b==c and c<a)) :
    print("El orden de los números de menor a mayor es: ",b,",",c,",",a)
if ((b<a and a<c) or (b==a and a<c) or (b<a and a==c)) :
    print("El orden de los números de menor a mayor es: ",b,",",a,",",c)
if ((c<a and a<b) or (c==a and a<b)) :
    print("El orden de los números de menor a mayor es: ",c,",",a,",",b)



