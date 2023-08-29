#EJERCICIO 1 H1-P1

num1 = int(input("Ingrese su primer número:"))
num2 = int(input("Ingrese su segundo número:"))
num3 = int(input("Ingrese su tercer número:"))

menor = min(num1,num2,num3)
mayor = max(num1,num2,num3)
numedio= (num1+num2+num3)-menor -mayor

print(menor,",",numedio,",",mayor)