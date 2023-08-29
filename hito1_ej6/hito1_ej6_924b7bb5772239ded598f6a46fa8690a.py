#Ordenar tres números

num1 = int(input("Numero: "))
num2 = int(input("Numero: "))
num3 = int(input("Numero: "))

numbers = [num1, num2, num3]
numbers.sort()


en_orden = ",".join(str(num) for num in numbers)

print(en_orden)
 




      