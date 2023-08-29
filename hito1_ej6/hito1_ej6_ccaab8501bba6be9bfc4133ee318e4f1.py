#Ordenar tres números
x=int(input("escriba un numero de 2 digitos: "))
y=int(input("escriba otro numero de 2 digitos: "))
z=int(input("escriba un tercer numero de 2 digitos: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("el orden es:{},{},{}".format(a,b,c))