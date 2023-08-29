#Entrada

print("Números ordenados de mayor a menor.")

mayor = mediano = menor = aa = int(input("Ingrese un número: "))
mayor = mediano = menor = bb = int(input("Ingrese un número: "))
mayor = mediano = menor = cc = int(input("Ingrese un número: "))

if bb < aa > cc :
    mayor = aa
elif aa < bb > cc :
    mayor = bb
elif aa < cc > bb :
    mayor = cc

if bb < aa < cc :
    mediano = aa
elif bb > aa > cc:
    mediano = aa
elif aa < bb < cc :
    mediano = bb
elif aa > bb > cc :
    mediano = bb
elif aa < cc < bb:
    mediano = cc
elif aa > cc > bb :
    mediano = cc

if bb > aa < cc :
    menor = aa
elif aa > bb < cc :
    menor = bb
elif aa > cc < bb :
    menor = cc

print(menor,mediano,mayor, sep=",")