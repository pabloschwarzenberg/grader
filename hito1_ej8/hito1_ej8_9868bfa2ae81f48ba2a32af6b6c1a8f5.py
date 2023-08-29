#Descomponer un número
numero = int(input("ingresa un numero de 4 digitos: "))
num = numero
m = numero//1000
numero = numero%1000
c = numero//100
numero = numero%100
d = numero//10
u = numero%10

print("Para ",num," es: ",m,"M + ",c,"C + ",d,"D + ",u,"U")      