#Ordenar tres números
#entradas
a = int(input("ingrese el valor de a:"))
b = int(input("ingrese el valor de b:"))
c = int(input("ingrese el valor de c:"))
#condicion
if (a<=b<=c):
    print("los numeros ordenados son:", a,",",b,",",c)
elif(a<=c<=b):
    print("los numeros ordenados son:", a,",",c,",",b)
elif(b<=a<=c):
    print("los numeros ordenados son:", b,",",a,",",c)
elif(b<=c<=a):
    print("los numeros ordenados son:", b,",",c,",",a)
elif(c<=a<=b):
    print("los numeros ordenados son:", c,",",a,",",b)
elif(c<=b<=a):
    print("los numeros ordenados son:", c,",",b,",",a)

