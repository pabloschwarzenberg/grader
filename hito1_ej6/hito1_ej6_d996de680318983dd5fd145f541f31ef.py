#Ordenar tres números
x=int(input("escriba el priemr numero entero"))
y=int(input("escriba el segundo nemro entero"))
z=int(input("escriba el tercer numero entero"))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("los numeros ordenados son: {},{},{}".format(a,b,c))