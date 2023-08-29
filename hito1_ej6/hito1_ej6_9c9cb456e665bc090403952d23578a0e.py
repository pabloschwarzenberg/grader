#Ordenar tres números
n= int (input("escriba el primer numero:"))
r= int(input("escriba el segundo numero:"))
z= int(input(" escriba el tercer numero:"))

a= min(n, r, z)
v= max(n, r, z) 
b= (n + r + z) -a -v

print("el orden de los numeros enteros son los siguientes: {}, {}, {}". format (a,b,v))      