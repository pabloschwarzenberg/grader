#Descomponer un número      
x=60000000000
while(x>9999):
 x=int(input("ingrese un numero de 4 digitos: "))
print(x//1000, "M", "+", ((x%1000)//100), "C", "+", ((x%100)//10), "D", "+", x-(x//10)*10, "U")