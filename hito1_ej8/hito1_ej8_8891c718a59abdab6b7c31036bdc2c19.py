#Descomponer un número

numero = eval(input("Introduce una cifra de hasta 4 dígitos: "))

umil = round(numero / 1000,)
tmp = numero % 1000

centenas = round(tmp / 100,)
tmp = tmp % 100

decenas = round(tmp / 10)
unidades = tmp % 10


print("Cifra: ",umil,"+",centenas,"+",decenas,"+",unidades)