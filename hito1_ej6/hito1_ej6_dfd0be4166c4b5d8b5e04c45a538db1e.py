#Ordenar tres números
num1=int(input("ingresa el primer numero: "))
num2=int(input("ingresa el segundo numero: "))
num3=int(input("ingresa el tercer numero: "))

Mi=min(num1, num2, num3)
Ma=max(num1, num2, num3)
c=(num1+num2+num3)-Ma-Mi

print("De menor a mayor el orden de los numeros ingresados es ", Mi ,",", c , ",", Ma)
