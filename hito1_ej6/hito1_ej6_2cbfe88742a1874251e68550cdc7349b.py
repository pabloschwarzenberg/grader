#Ordenar tres números

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

mayor = max(num1,num2,num3)
menor = min(num1,num2,num3)
medio= num1 + num2 + num3-mayor-menor

print(str(menor)+"," + str(medio)+ ","+ str(mayor))