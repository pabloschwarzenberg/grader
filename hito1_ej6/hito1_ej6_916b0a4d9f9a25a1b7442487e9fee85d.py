print("Ordenar tres números")
X=int(input("Ingrese primer número:"))
Y=int(input("Ingrese segundo número:"))
Z=int(input("Ingrese tercer número:"))
a=min(X,Y,Z)
b=max(X,Y,Z)
c=(X+Y+Z)-a-b
print(a,",",c,",",b)      