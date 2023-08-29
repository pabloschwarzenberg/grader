#Ordenar tres números
x=int(input("Ingrese el primer número entero:"))
y=int(input("Ingrese el segundo número entero:"))
z=int(input("Ingrese el tercer número entero:"))

if(x>=y>=z): print(z,",",y,",",x)
elif(x>=z>=y): print(y,",",z,",",x)
elif(y>=x>=z): print(z,",",x,",",y)
elif(y>=z>=x): print(x,",",z,",",y)
elif(z>=y>=x): print(x,",",y,",",z)
elif(z>=x>=y): print(y,",",x,",",z)