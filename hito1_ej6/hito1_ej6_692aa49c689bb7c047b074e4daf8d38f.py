#Ordenar tres números
a = int(input("Ingrese un numero:"))
b = int(input("Ingrese un numero:"))
c = int(input("Ingrese un numero:"))
Maximo = max(a,b,c)
Minimo = min(a,b,c)
d = (a+b+c)-Maximo-Minimo
print("el orden de estos numeros de menor a mayor es",Minimo,",",d,",",Maximo)