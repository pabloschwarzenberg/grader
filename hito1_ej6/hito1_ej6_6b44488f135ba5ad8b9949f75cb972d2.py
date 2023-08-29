#Ordenar tres números
x=input("Ingrese el primer numero: ")
y=input("Ingrese el segundo numero: ")
z=input("Ingrese el tercer numero: ")
if x>=y>=z:
    print(str(z)+","+str(y)+","+str(x))
if x>=z>=y:
    print(str(y)+","+str(z)+","+str(x))
if y>=x>=z:
    print(str(z)+","+str(x)+","+str(y))
if y>=z>=x:
    print(str(x)+","+str(z)+","+str(y))
if z>=x>=y:
    print(str(y)+","+str(x)+","+str(z))
if z>=y>=x:
    print(str(x)+","+str(y)+","+str(z))