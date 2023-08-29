#Ordenar tres números
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
numero1 = int(input("ingrese un numero(1):"))
numero2 = int(input("ingrese un numero(2):"))
numero3 = int(input("ingrese un numero(3):"))

if(numero1 == numero2 == numero3):
    
    print(numero1,",",numero2,",",numero3)
else:
    if(numero1 == numero2 < numero3):
         print(numero1,",",numero2,",",numero3)
    if(numero3 == numero2 < numero1):
         print(numero3,",",numero2,",",numero1)
    if(numero3 == numero1 < numero2):
         print(numero3,",",numero1,",",numero2)
    if(numero1 == numero2 > numero3):
         print(numero3,",",numero1,",",numero2)
    if(numero1 == numero3 > numero2):
        print(numero2,",",numero1,",",numero3)
    if(numero3 == numero2 > numero1):
        print(numero3,",",numero2,",",numero1)
    if(numero3 < numero1 < numero2):
         print(numero3,",",numero1,",",numero2)
    if(numero3 < numero2 < numero1):
         print(numero3,",",numero2,",",numero1)
    if(numero2 < numero3 < numero1):
         print(numero2,",",numero3,",",numero1)
    if(numero2 < numero1 < numero3):
         print(numero2,",",numero1,",",numero3)
    if(numero1 < numero2 < numero3):
         print(numero1,",",numero2,",",numero3)
    if(numero1 < numero3 < numero2):
         print(numero1,",",numero3,",",numero2)
