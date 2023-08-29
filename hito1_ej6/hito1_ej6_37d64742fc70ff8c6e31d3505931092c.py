#Ordenar tres números
x = int(input("Ingrese primer numero :"))
y = int(input("Ingrese segundo numero :"))
z = int(input("Ingrese tercer numero :"))
var1 = min(x , y , z)
var2 = max(x , y , z)
var3 = (x + y + z) - var1 - var2
print("El orden de los numeros es" , var1 , "," , var3 , "," , var2)