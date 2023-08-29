#Descomponer un número
num=eval(input("ingrese un numero de hasta 4 digitos: "))
miles=num//1000
num=num%1000
centenas=num//100
num=num%100
decenas=num//10
num=num%10
unidad=num//1
num=num%1
print(miles,"M +",centenas,"C +",decenas,"D +",unidad,"U")      