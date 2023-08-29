#Ordenar tres números
a = int(input("ingrese un primer valor:"))
b = int(input("ingrese un segundo valor:"))
c = int(input("ingrese un tercer valor:"))

X = min(a,b,c)
Z = max(a,b,c)
Y = (a+b+c)-X-Z
print("los numeros ordenados son {},{},{}".format(X,Y,Z))