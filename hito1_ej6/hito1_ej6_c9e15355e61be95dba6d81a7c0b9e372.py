a= int(input("ingrese el primer numero: "))
b= int(input("ingrese el segundo numero: "))
c= int(input("ingrese el tercer numero numero: "))
# Caso numeros distintos
if (a<b and b<c):
    print ("Los numeros ordenados de menor a mayor son: ",a,",",b,",",c)
elif (a<c and c<b):
    print("Los numeros ordenados de menor a mayor son: ",a,",",c,",",b)
elif (b<a and a<c):
    print("Los numeros ordenados de menor a mayor son: ",b,",",a,",",c)
elif (b<c and c<a):
    print("Los numeros ordenados de menor a mayor son: ",b,",",c,",",a)
elif (c<b and b<a):
    print("Los numeros ordenados de menor a mayor son: ",c,",",b,",",a)
elif (c<a and a<b):
    print("Los numeros ordenados de menor a mayor son: ",c,",",a,",",b)
# Caso, variables repetidas
elif (a==b and b<c):
    print("Los numeros ordenados de menor a mayor son: ",a,",",b,",",c)
elif (a==c and c<b):
    print("Los numeros ordenados de menor a mayor son: ",a,",",c,",",b)
elif (b==a and a<c):
    print("Los numeros ordenados de menor a mayor son: ",b,",",a,",",c)
elif (b==c and c<a):
    print("Los numeros ordenados de menor a mayor son: ",b,",",c,",",a)
elif (c==b and b<a):
    print("Los numeros ordenados de menor a mayor son: ",c,",",b,",",a)
elif (c==a and a<b):
    print("Los numeros ordenados de menor a mayor son: ",c,",",a,",",b)
#Caso, todas las variables repetidas
else:
    print("¡Todos los numeros son iguales!")
