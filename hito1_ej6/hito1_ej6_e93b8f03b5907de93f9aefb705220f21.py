import random
numero1 = int(input("ingrese un numero: "))
print(numero1)
numero2 = int(input("ingrese un numero: "))
print(numero2)
numero3 = int(input("ingrese un numero: "))
print(numero3)
if numero1 <= numero2 <= numero3 :
    print(numero1,numero2,numero3,sep=",")
elif numero1 <= numero3 <= numero2 :
    print(numero1,numero3,numero2,sep=",")
elif numero2 <= numero1 <= numero3 :
    print(numero2,numero1,numero3,sep=",")
elif numero2 <= numero3 <= numero1 :
    print(numero2,numero3,numero1,sep=",")
elif numero3 <= numero1 <= numero2 :
    print(numero3,numero1,numero2,sep=",")
elif numero3 <= numero2 <= numero1 :
    print(numero3,numero2,numero1,sep=",")
print("Fin del comando")