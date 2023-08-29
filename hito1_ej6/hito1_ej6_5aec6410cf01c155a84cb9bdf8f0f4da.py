#Ordenar tres números
x = int (input("ingrese un numero entero"))
y = int (input("ingrese un numero entero"))
z = int (input("ingrese un numero entero"))
a = min(x,y,z)
c = max(x,y,z)
b =(x+y+z)-a-c
print(a,",",b,",",c)