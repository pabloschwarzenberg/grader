#Ordenar tres números
num1  = int(input("numero 1: "))
num2  = int(input("numero 1: "))  
num3  = int(input("numero 1: ")) 

max1 = max(num1, num2, num3)
min1 = min(num1, num2, num3)
mid = num1 + num2 + num3 - max1 - min1

print(min1,",", mid,",", max1)