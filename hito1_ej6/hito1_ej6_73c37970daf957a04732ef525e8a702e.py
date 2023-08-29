#Ordenar tres números
#Primero vamos a ingresar las primeras 3 variables
x = eval(input("Ingrese el primer número entero"))
y = eval(input("Ingrese el segundo número entero"))
z = eval(input("Ingrese el tercer número entero"))

#Ahora ordenamos de mayor a menor

MA = max(x,y,z)
MI = min(x,y,z)
N = ((x + y + z) - MA - MI)
#Ahora deberia ordenarse

print("Los valores ordenados de menor a mayor son: ",MI,",",N,",",MA)