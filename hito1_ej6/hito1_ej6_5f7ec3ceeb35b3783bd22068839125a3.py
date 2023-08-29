#Ordenar tres números
numero1 = int(input("ingrese numero 1: "))
numero2 = int(input("ingrese numero 2: "))
numero3 = int(input("ingrese numero 3: "))
menor = numero1
mayor = numero1
if menor > numero2:
    menor = numero2
if mayor < numero2:
    mayor = numero2
if menor > numero3:
    menor = numero3
if mayor < numero3:
    mayor = numero3
total = numero1+numero2+numero3
x = total - mayor - menor
print(menor,x,mayor,sep=', ')