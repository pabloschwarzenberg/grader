"""
1.- Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a
mayor, separados por una coma.
"""

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
numero3 = int(input("Número 3: "))

if numero1 > numero2:
    if numero1 > numero3:
        if numero2 > numero3:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero3+", "+numero2+", "+numero1)
        else:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero2+", "+numero3+", "+numero1)
    else:
        if numero1 > numero2:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero2+", "+numero1+", "+numero3)
        else:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero1+", "+numero2+", "+numero3)
else:
    if numero2 > numero3:
        if numero1 > numero3:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero3+", "+numero1+", "+numero2)
        else:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero1+", "+numero3+", "+numero2)
    else:
        if numero1 > numero2:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero2+", "+numero1+", "+numero3)
        else:
            numero1 = str(numero1)
            numero2 = str(numero2)
            numero3 = str(numero3)
            print(numero1+", "+numero2+", "+numero3)
        
