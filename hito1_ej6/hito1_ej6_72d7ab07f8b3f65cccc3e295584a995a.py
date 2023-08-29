#Ordenar tres números
x=int(input("ingrese el primer numero: "))
y=int(input("ingrese el segundo numero: "))
z=int(input("ingrese el tercer numero: "))

a=min(x,y,z)
b=max(x,y,z)
c= (x+y+z)-a-b

print("los numeros ordenados son: {}, {} , {} ".format(a,c,b))
