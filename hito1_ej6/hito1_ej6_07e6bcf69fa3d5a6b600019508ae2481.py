#Ordenar tres números
import math
numero1 = eval(input("Ingrese un número a continuación: "))
numero2 = eval(input("Ahora, ingrese un número distinto al anterior: "))
numero3 = eval(input("Finalmente, ingrese un número que sea disstinto a los 2 anteriores: "))

if(numero1 < numero2 and numero2 < numero3):
    print("{},{},{}" .format(numero1, numero2, numero3))

if(numero2 < numero1 and numero1 < numero3):
    print("{},{},{}" .format(numero2, numero1, numero3))

if(numero3 < numero1 and numero1 < numero2):
    print("{},{},{}" .format(numero3, numero1, numero2))

if(numero3 < numero2 and numero2 < numero1):
    print("{},{},{}" .format(numero3, numero2, numero1))

if(numero1 < numero3 and numero3 < numero2):
    print("{},{},{}" .format(numero1, numero3, numero2))

if(numero2 < numero3 and numero3 < numero1):
    print("{},{},{}" .format(numero2, numero3, numero1))
    
if(numero1 == numero2 and numero1 < numero3):
    print("{},{},{}" .format(numero1, numero2 ,numero3))
    
if(numero1 == numero3 and numero1 > numero2):
    print("{},{},{}" .format(numero2, numero1, numero3))

if(numero1 == numero3 and numero1 < numero2):
    print("{},{},{}" .format(numero1, numero3, numero2))
    