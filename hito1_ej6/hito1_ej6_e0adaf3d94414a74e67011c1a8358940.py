#Ordenar tres números
a = int(input("Ingresar primer número: \n"))
b = int(input("Ingresar Segundo número: \n"))
c = int(input("Ingresar tercer número: \n"))

mayor = max(a,b,c)
minimo = min(a,b,c)
intermedio = (a + b + c) - mayor - minimo 
print((minimo,intermedio,mayor))