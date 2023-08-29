#Ordenar tres números
x=int(input("Ingrese número 1 :"))
y=int(input("Ingrese número 2 :"))
z=int(input("Ingrese número 3 :"))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c

print("Tus números ahora ordenados de mayor a menor son los siguientes : "+str(a)+", "+str(b)+", "+str(c))