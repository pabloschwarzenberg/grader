#Cálculo de orden númerico 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))


num_menor = min(num1,num2,num3)
num_mayor = max(num1, num2, num3)
num_medio = (num1+num2+num3)- num_mayor - num_menor

print("Los números son: ",num_menor,",",num_medio,",",num_mayor) 

