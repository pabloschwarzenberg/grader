print("Considerando una ecuación lineal como: ax + by = c : \n")


a = int(input("Ingrese el valor de a: \n"))
b = int(input("Ingrese el valor de b: \n"))
c = int(input("Ingrese el valor de c: \n"))
d = int(input("Ingrese el valor de d: \n"))
e = int(input("Ingrese el valor de e: \n"))
f = int(input("Ingrese el valor de f: \n"))


print("Para el siguiente sistema: \n")
print("Ecuación 1;",a,"x +",b,"y =",c)
print("Ecuación 2;",d,"x +",e,"y =",f)
print("\n La solución es:")

determinante = a*e - b*d
x = x = round(((c*e - b*f)/determinante),2)
y = round(((a*f - c*d)/determinante),2)


print("x =",x,"y = ",y)