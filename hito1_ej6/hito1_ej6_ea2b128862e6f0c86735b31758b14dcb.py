#Ordenar tres números
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))
 
ma = max(a,b,c)
mi = min(a,b,c)
me = (a + b + c) -ma -mi
 
print("El orden de los numero de menor a mayor es: " , mi , "," , me , "," ,ma)