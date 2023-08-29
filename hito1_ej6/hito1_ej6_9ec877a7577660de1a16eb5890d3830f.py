#Ordenar tres números
x = int(input("ingresa el primer numero: "))
y = int(input("ingresa el segundo numero: "))
z = int(input("ingresa el tercer numero. "))

a= min(x,y,z)
c= max(x,y,z)
b= (x+y+z)-a-c

print("los numeros ordenados son:{}, {}, {}".format(a,b,c))
            