#Ordenar tres números
x= int(input("escriba primer numero, "))
y= int(input("escriba segundo numero, "))
z= int(input("escriba tercer numero, "))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print("el orden de menor a mayor es ", a ," , ", b , " , ", c)