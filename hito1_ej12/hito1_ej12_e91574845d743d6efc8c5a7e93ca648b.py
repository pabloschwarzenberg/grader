import random
nc= random.randint(1,20)
for i in range(5):
    ni=int(input("Ingrese un número entre el 1 y el 20:"))
    if nc==ni:
        a=print("Adivinaste, mi número era", nc)
        break
    elif nc<ni:
        print("El numero es menor")
    elif nc>ni:
        print ("El numero es mayor")
if nc!=ni:
    print("No adivinaste, mi número era", nc)
