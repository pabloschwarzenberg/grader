#Descomponer un número
n = int(input("Ingrese un número entero de hasta 4 dígitos: "))

miles = n//1000

centenas = (n - miles*1000)//100

decenas = (n - miles*1000 - centenas*100)//10

unidades = (n - miles*1000 - centenas*100 - decenas*10)

print(miles,"M +",centenas,"C +",decenas,"D +",unidades,"U")