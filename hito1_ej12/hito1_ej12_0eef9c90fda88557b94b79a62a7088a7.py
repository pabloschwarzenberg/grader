#Juego adivina mi número
import random
numsec = random.randint(1,20)
print(numsec)
conta = 1
inte = 4
num = int(input("Ingrese un número del 1 al 20: "))
while inte != 0:
    if (numsec < num):
        print("Te quedan",inte, "intentos.")
        print("Ingresa un número menor")
        num = int(input("Ingresa un número menor: "))
        inte -= 1
        
    if (numsec > num):
        print("Te quedan",inte ,"intentos.")
        print("Ingresa un número mayor")
        num = int(input("Ingrese un número del 1 al 20: "))
        conta = conta + 1
        
        inte -= 1

    if(num == numsec):
        print('Adivinaste, mi número era', numsec)
    
if inte == 0:
   print('No adivinaste, mi número era', numsec)