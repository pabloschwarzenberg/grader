#Descomponer un número
numero=int(input("ingresa numero de 4 cifras:"))

unidad=numero%10
decimal=(numero%100-numero%10)//10
centecima=(numero%1000-numero%100)//100
milecima=(numero%10000-numero%1000)//1000

print(unidad,"U")
print(decimal,"D")
print(centecima,"C")
print(milecima,"M")
