#Ordenar tres números
x= int(input("escoge el primer numero: "))
y= int(input("escoge el segundo numero: "))
z= int(input("escoge el tercer numero: "))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)- a - c

print("los numeros ordenados son: ", a,",",b,",", c)    