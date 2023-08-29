#Descomponer un número
print ("Introduce el número: ")
numero = int(input())

umil = numero // 1000
tmp = numero % 1000

c = tmp // 100
tmp = tmp % 100

d = tmp // 10
u = tmp % 10

print (umil,"M+",c,"C+",d,"D+",u,"U")
