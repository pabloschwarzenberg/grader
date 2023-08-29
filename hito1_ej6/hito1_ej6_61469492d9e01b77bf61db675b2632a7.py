#Ordenar tres números
x= int (input("escribe el primer numero: "))
y= int (input("escribe el segundo numero: "))
z= int (input("escribe el tercer numero: "))     

a = min(x,y,z)
c = max (x,y,z)
b = (x + y + z) -a - c

print("los numeros de mayor a menor son: {}, {}, {}".format (a,b,c))

