numero = eval(input("ingrese un numero de 4 cifras"))



millares = (numero//1000)%10
centenas = (numero//100)%10
decenas = (numero//10)%10
unidades = (numero//1)%10

print(millares,"M+", centenas,"C+", decenas,"D+",unidades,"U",)