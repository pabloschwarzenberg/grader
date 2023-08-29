#Ordenar tres números
a = int(input("ingrese un numero: "))      
b = int(input("ingrese un segundo numero: ")) 
c = int(input("ingrese un tercer numero: ")) 

x = min (a,b,c)
y = max (a,b,c)
z = (a+b+c) - x - y

print ("numeros ordenados",  (x,z,y))