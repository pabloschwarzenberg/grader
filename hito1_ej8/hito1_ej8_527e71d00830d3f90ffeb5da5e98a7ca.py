#Descomponer un número
num = eval (input("Ingrese un número de 4 digitos \n "))
miles = (num//1000) %10
centenas = (num//100)%10
decenas = (num//10)%10
unidades = (num//1)%10

print (miles,"M+",centenas,"C+",decenas,"D+",unidades,"U",)   