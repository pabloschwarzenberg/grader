#ordene 3 numeros
#definir variables
v1 = int(input("ingrese el primer numero:"))
v2 = int(input("ingrese el segundo numero:"))
v3 = int(input("ingrese el tercer numero:"))
#ordenar el menor y el mayor
x = min(v1, v2, v3)
y = max(v1, v2, v3)
#el numero del medio
z = (v1 + v2 + v3) - x - y 
#imprimir el el orden
#print("el numero menor es:", x,"el de al medio es:", y,"y el mayor es:", z)
print(x,",",z,",",y)