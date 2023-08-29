#Juego Adivina mi número secreto
import random
numsec = random.randint(1, 20)
#print (numsec)
print ("Adivina mi número, es desde el 1 hasta el 20, tienes 5 intentos.")

int1 = (int(input("Intento 1: ")))
if int1 == numsec:
    print ("Adivinaste, mi número era " + str(numsec))
    exit()
elif int1 > numsec:
    print ("Mi número es menor.")
else:
    print ("Mi número es mayor.")

int2 = (int(input("Intento 2: ")))

if int2 == numsec:
    print ("Adivinaste, mi número era " + str(numsec))
    exit()
elif int2 > numsec:
    print ("Mi número es menor.")
else:
    print ("Mi número es mayor.")

int3 = (int(input("Intento 3: ")))

if int3 == numsec:
    print ("Adivinaste, mi número era " + str(numsec))
    exit()
elif int3 > numsec:
    print ("Mi número es menor.")
else:
    print ("Mi número es mayor.")

int4 = (int(input("Intento 4: ")))

if int4 == numsec:
    print ("Adivinaste, mi número era " + str(numsec))
    exit()
elif int4 > numsec:
    print ("Mi número es menor.")
else:
    print ("Mi número es mayor.")

int5= (int(input("Intento 5: ")))

if int5 == numsec:
    print ("Adivinaste, mi número era " + str(numsec))
    exit()
else:
    print ("No adivinaste, mi número era " + str(numsec))
      